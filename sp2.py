from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)
# print("Running in headless mode...")
# driver.quit()
# import requests
# resp = requests.get("https://api.github.com")
# assert resp.status_code == 200
# driver= webdriver.Chrome()  # Ensure chromedriver is in PATH
# driver.get("https://www.github.com")
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#     def login(self, user, pwd):
#         self.driver.find_element(By.ID, "username").send_keys(user)
#         self.driver.find_element(By.ID, "password").send_keys(pwd)
#         self.driver.find_element(By.ID, "loginBtn").click()
# #driver.quit()
# # Ensure the driver is closed after use  
# driver.quit()

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--disable-gpu")  # For Windows
chrome_options.add_argument("--window-size=1920,1080")  # Optional

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://127.0.0.1:5500/basic_site.html?#")

print("Page Title:", driver.title)

driver.quit()
