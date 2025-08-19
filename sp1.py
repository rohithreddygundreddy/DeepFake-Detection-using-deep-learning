from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Path to your local HTML file
file_path = os.path.abspath("basic_site.html")
url = f"http://127.0.0.1:5500/basic_site.html?#"

driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
driver.get(url)

# Click the "Login" link
login_link = driver.find_element(By.LINK_TEXT, "Login")
login_link.click()
time.sleep(1)

# Fill in the login form
username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
username.send_keys("testuser")
password.send_keys("testpass")

# Click the "Login" button
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
login_button.click()
time.sleep(1)
alert=driver.switch_to.alert
alert.accept() 
time.sleep(1)
# Check if still on login page (since no backend, page won't change)
login_header = driver.find_element(By.XPATH, "//h2[text()='Login']")
if login_header.is_displayed():
    print("Login page works and form submitted (no backend, so stays on page).")
else:
    print("Login page did not work as expected.")

driver.quit()