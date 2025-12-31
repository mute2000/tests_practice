import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestHogwarts():
    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        time.sleep(3)
        self.driver.quit()

    def test_hogwarts(self):
        category_link = (By.XPATH, "//*[text()='分类' or contains(text(), '分类')]")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(category_link) 
        )
        self.driver.find_element(*category_link).click() 

        category_name = (By.CSS_SELECTOR, ".category-name")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(category_name)
        )
        self.driver.find_element(*category_name).click() 