"""
write: terence 
create date :2024/2/16 
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

path = "chromedriver.exe"
service = Service(path)
options = Options()
options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=options, service=service, keep_alive=True)
browser.get("https://www.baidu.com")
# 获取获取百度一下按键
button = browser.find_element("id", "su")
# 获取百度搜索框
input_content = browser.find_element("id", "kw")
input_content.send_keys("周杰伦")
time.sleep(2)
button.click()
time.sleep(2)
js_script = "document.documentElement.scrollTo = 10000"
browser.execute_script(js_script)
time.sleep(2)
# 找到下一页按钮
next_page = browser.find_element(By.CLASS_NAME, "n")
# 按下下一页按钮
next_page.click()
time.sleep(2)
# 回退上一页
browser.back()
time.sleep(2)
# 往前一页
browser.forward()
time.sleep(10)
