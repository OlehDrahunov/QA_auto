import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui1
def test_check_incorrect_username():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://github.com/login")
    login_element = driver.find_element(By.ID, "login_field")
    login_element.send_keys("non_existing_user@gmail.com")
    pass_element = driver.find_element(By.ID, "password")
    pass_element.send_keys("wrong password")
    driver.find_element(By.NAME, "commit").click()
    assert driver.title == "Sign in to GitHub · GitHub"
    driver.close()