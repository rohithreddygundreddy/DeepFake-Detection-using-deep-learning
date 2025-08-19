from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.com")

elements = driver.find_elements(By.TAG_NAME, "li")
texts_upper = list(map(lambda e: e.text.upper(), elements))
print(texts_upper)

import pytest

@pytest.fixture
def sample_data():
    return {"username": "testuser", "password": "12345"}

def test_user_data(sample_data):
    assert sample_data["username"] == "testuser"
test_user_data({"username": "testuser", "password": "12345"})