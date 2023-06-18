from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest


@pytest.mark.usefixtures("headless_setup")
class TestLogin:
    def test_demo(self):
        features = self.driver.find_element(By.LINK_TEXT,"Demo")
        features.click()
        expected = "https://www.opencart.com/index.php?route=cms/feature"
        assert self.driver.current_url.__eq__(expected)