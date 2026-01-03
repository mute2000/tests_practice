from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化Firefox驱动
driver = webdriver.Firefox()

try:
    # 1. 访问豆瓣电影首页
    driver.get("https://movie.douban.com/")
    driver.maximize_window()  # 窗口最大化
    print("✅ 成功打开豆瓣电影")

    # 2. 显式等待搜索框加载（解决元素未就绪问题）
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "search_text"))
    )

    # 3. 输入操作：搜索框输入电影名
    search_box.send_keys("哪吒之魔童闹海")
    time.sleep(1)
    print("✅ 成功输入搜索内容")

    # 4. 点击操作：点击搜索按钮
    search_btn = driver.find_element(By.CLASS_NAME, "inp-btn")
    search_btn.click()
    time.sleep(2)
    print("✅ 成功点击搜索按钮，跳转到结果页")

    # 5. 获取元素属性：提取第一个搜索结果的标题
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".item-root a"))
    )
    movie_title = first_result.get_attribute("title")
    print(f"📌 第一个搜索结果标题：{movie_title}")

    # 6. 刷新页面操作
    driver.refresh()
    time.sleep(2)
    print("✅ 成功刷新页面")

    # 7. 窗口操作：设置窗口大小为800*600
    driver.set_window_size(800, 600)
    time.sleep(1)
    print("✅ 成功设置窗口大小")

    # 8. 清除输入（返回首页后操作）
    driver.back()  # 回到豆瓣电影首页
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "search_text"))
    )
    search_box.clear()
    print("✅ 成功清空搜索框")

except Exception as e:
    print(f"❌ 操作出错：{e}")

finally:
    # 9. 关闭浏览器
    time.sleep(2)
    driver.quit()
    print("🔚 浏览器已关闭")