from selenium import webdriver
import pytest
import time
import allure


@pytest.fixture()
def headless_setup(request):
    global driver
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    driver.get("https://www.opencart.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
