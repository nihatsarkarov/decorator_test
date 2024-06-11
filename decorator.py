import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

@pytest.fixture(scope="module")
def driver():
    service = Service("C:/Users/Q1/PythonAlgoritmika/Decorator/chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def logo_icon_element(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.logo__icon')))

@pytest.fixture(scope="module")
def cookies_div_element(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookies')))

@pytest.fixture(scope="module")
def login_form_element(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.login-form__container')))

def test_cookies_div_icon_logo_background_color(logo_icon_element):
    background_color = logo_icon_element.value_of_css_property("background-color")
    assert background_color == "rgba(0, 0, 0, 0)", f"Expected background color rgba(0, 0, 0, 0), but got {background_color}"

def test_cookies_div_properties(cookies_div_element):
    background_color = cookies_div_element.value_of_css_property("background-color")
    height = float(cookies_div_element.size['height'])
    assert background_color == "rgba(255, 255, 255, 1)", "Background color is not as expected"
    assert height == 155.0, "Height is not as expected"

def test_cookies_div_password_background_color(login_form_element):
    background_color = login_form_element.value_of_css_property("background-color")
    assert background_color == "rgba(255, 255, 255, 1)", "Background color is not as expected"

if __name__ == "__main__":
    pytest.main()
