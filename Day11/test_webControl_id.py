# webdriver是selenium库中负责操作浏览器的核心模块
from selenium import webdriver
# By是selenium库中负责定位元素的模块
from selenium.webdriver.common.by import By
#Python自带的时间处理模块
import time

# 创建火狐浏览器的驱动对象
driver = webdriver.Edge()
# Python的异常处理语句
try:
    driver.get("https://image.baidu.com/")
    # 隐式等待5秒
    driver.implicitly_wait(5)
    # 定位id为app的元素
    head_element = driver.find_element(By.ID, "app")
    print("✅ 成功定位到id为app的元素,Firefox环境配置正常!")
    print("元素信息：", head_element)

# 异常处理的错误捕获
except Exception as e:
    print("❌ 定位失败，问题原因：", e)

finally:
    # 停留3秒后关闭浏览器
    time.sleep(3)
    driver.quit()