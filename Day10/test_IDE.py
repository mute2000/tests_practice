import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDefaultSuite():
    # setup_module()只会在开始测试运行一次
    def setup_method(self, method):
        # 初始化webdriver
        self.driver = webdriver.Chrome()
        self.vars = {}
    # teardown_module()只会在结束测试运行一次
    def teardown_method(self, method):
        # 关闭浏览器并关闭启动ChromeDriver时启动的ChromeDriver可执行文件
        self.driver.quit()
    # 测试方法
    def test_ceshirendemo1(self):
        #访问网址
        self.driver.get("https://ceshiren.com/")
        #设置窗口大小
        self.driver.set_window_size(1296, 705)
        #点击操作
        self.driver.find_element(By.LINK_TEXT, "最新").click()
        self.driver.find_element(By.LINK_TEXT, "热门").click()
        self.driver.find_element(By.LINK_TEXT, "最新").click()
        self.driver.find_element(By.LINK_TEXT, "分类").click()
        #关闭当前窗口
        self.driver.close()