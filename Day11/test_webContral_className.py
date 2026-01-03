# 导入模块（省略，保持原有导入）
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# 主程序入口：只有手动运行脚本时才执行
if __name__ == "__main__":
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    try:
        driver.get("https://image.baidu.com/")
        driver.implicitly_wait(5)
        head_element = driver.find_element(By.CLASS_NAME, "cos-wise.cos-android")
        print("✅ 成功定位到核心元素,Firefox环境配置正常!")
        print("元素信息：", head_element)
    except Exception as e:
        print("❌ 定位失败，问题原因：", e)
    finally:
        time.sleep(3)
        driver.quit()