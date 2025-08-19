from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
quary= "laptop"
fileno=0
for i in range(1,2):
    driver.get(f"https://www.amazon.in/s?k={quary}&page={i}&xpid=seC19QaY0kpYO&crid=38KYQIWNFIK14&qid=1755155964&sprefix=laptop+%2Caps%2C579&ref=sr_pg_2")
    driver.save_screenshot(f"data/page_{i}.png") 
    ele=driver.find_elements(By.CLASS_NAME,"sg-col-inner")
    print(f"{len(ele)} items found")
for a in ele:
    d = a.get_attribute("innerHTML")
        #print(a.text)
    with open(f"data/{quary}_{fileno}.html", "w", encoding="utf-8") as file:
        file.write(d)
        fileno+=1
#print(ele.get_attribute("innerHTML"))
time.sleep(2)
#driver.save_screenshot("file.png")
print(driver.delete_all_cookies())
#driver.add_cookie()
#driver.delete_all_cookies().
driver.close()

