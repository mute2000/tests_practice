import allure
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.edge.service import Service  # 补充导入Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data1", yaml.safe_load(open("./data/data.yaml", encoding="utf-8")))
def test_steps_demo(test_data1):
    driver = None  # 初始化driver变量
    try:
        with allure.step("打开百度网页"):
            # 修正Edge驱动初始化
            driver = webdriver.Edge(service=Service(r"C:\Users\Mute\Downloads\edgedriver_win64\msedgedriver.exe"))
            driver.get("http://www.baidu.com")
            driver.maximize_window()
        
        with allure.step(f"输入搜索词: {test_data1}"):
            driver.find_element(By.ID, "kw").send_keys(test_data1)
            time.sleep(2)
        
        with allure.step("点击搜索"):
            driver.find_element(By.ID, "su").click()
            time.sleep(2)
    finally:
        # 确保浏览器关闭
        if driver:
            driver.quit()