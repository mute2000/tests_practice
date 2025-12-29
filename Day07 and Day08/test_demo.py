import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# 读取 data.yaml 测试数据
def get_test_data():
    with open("./data/data.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data

# 定义测试类
@allure.feature("百度搜索功能测试")
class TestBaiduSearch:
    # 固件：初始化 Edge 浏览器
    def setup_class(self):
        # 初始化 Edge 驱动（若未配置环境变量，需指定 driver 路径，例如 Service(r"D:\msedgedriver.exe")）
        self.service = Service()
        self.driver = webdriver.Edge(service=self.service)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.wait = WebDriverWait(self.driver, 10)  # 显式等待10秒

    # 固件：关闭浏览器
    def teardown_class(self):
        self.driver.quit()

    # 参数化测试用例，读取 yaml 数据
    @allure.story("关键词搜索验证")
    @pytest.mark.parametrize("keyword", get_test_data())
    def test_search(self, keyword):
        # 1. 定位搜索框并输入关键词
        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "kw"))
        )
        search_box.clear()  # 清空输入框
        search_box.send_keys(keyword)
        allure.attach(f"输入搜索关键词：{keyword}", name="操作步骤", attachment_type=allure.attachment_type.TEXT)

        # 2. 定位搜索按钮并点击
        search_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "su"))
        )
        search_btn.click()

        # 3. 断言：搜索结果页标题包含关键词
        self.wait.until(
            EC.title_contains(keyword)
        )
        assert keyword in self.driver.title, f"搜索结果标题未包含关键词：{keyword}"
        allure.attach(self.driver.get_screenshot_as_png(), name=f"搜索{keyword}结果截图", attachment_type=allure.attachment_type.PNG)