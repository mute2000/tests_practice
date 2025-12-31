from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search():
    # 初始化火狐浏览器驱动（Windows下geckodriver需配置到环境变量，或指定路径）
    driver = webdriver.Firefox()
        # 打开百度首页
    driver.get('https://www.baidu.com')
        # 定位百度搜索按钮，获取其value属性（新版Selenium用By.ID）
    search = driver.find_element(By.ID, 'su').get_attribute('value')
    assert search == "百度"
        # 无论断言是否成功，都关闭浏览器
    driver.quit()