from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化Firefox驱动（适配火狐浏览器）
driver = webdriver.Firefox()

# 访问百度首页
driver.get('https://www.baidu.com')

# ========== 获取元素属性、坐标、大小（整合到变量） ==========
# 定位百度搜索按钮
search_btn = driver.find_element(By.ID, 'su')
# 整合获取属性、坐标、大小
attr_value = search_btn.get_attribute('value')
location = search_btn.location
size = search_btn.size
# 打印结果
print(attr_value)
print(location)
print(size)

# ========== 获取网页源代码、刷新页面（整合到变量） ==========
# 刷新页面
driver.refresh()
# 获取网页源代码
page_code = driver.page_source
# 打印网页源代码（可只打印前500字符，避免输出过长）
print(page_code[:500])

# 关闭浏览器
driver.quit()