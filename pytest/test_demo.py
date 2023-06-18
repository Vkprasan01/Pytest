import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import pytest


@pytest.mark.usefixtures("headless_setup")
class TestDemo:
    def test_features(self):
        features = self.driver.find_element(By.LINK_TEXT,"Features")
        features.click()
        expected = "https://www.opencart.com/index.php?route=cms/feature"
        assert self.driver.current_url.__eq__(expected)
        allure.attach(self.driver.get_screenshot_as_png(),name="test_features",attachment_type=AttachmentType.PNG)
