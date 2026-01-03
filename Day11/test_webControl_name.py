# webdriver是selenium库中负责操作浏览器的核心模块
from selenium import webdriver
# By是selenium库中负责定位元素的模块
from selenium.webdriver.common.by import By
#Python自带的时间处理模块
import time

# 创建火狐浏览器的驱动对象
driver = webdriver.Firefox()
# Python的异常处理语句
try:
    # 访问百度首页
    driver.get("https://image.baidu.com/")
    # 隐式等待5秒，确保元素加载
    driver.implicitly_wait(5)
    head_element = driver.find_element(By.NAME, "viewport")
    print("✅ 成功定位到name为viewport的元素,Firefox环境配置正常!")
    print("元素信息：", head_element)

except Exception as e:
    print("❌ 定位失败，问题原因：", e)

finally:
    # 停留3秒后关闭浏览器
    time.sleep(3)
    driver.quit()