"""
write: terence 
create date :2024/2/15 
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument('--start-maximized')
# options.add_argument('--disable-extensions')
path = "chromedriver.exe"
service = Service(path)
browser = webdriver.Chrome(options=options, service=service, keep_alive=True)
browser.get("http://www.baidu.com")
page_source = browser.page_source
text1 = browser.find_element(by=By.LINK_TEXT, value="hao123")
print(text1.get_attribute("href"))
# get button element id value == su
button = browser.find_element(By.ID, 'su')
browser.execute_script("console.log('selenium!')")
# wk = browser.find_element(By.ID,"kw")
wk = browser.find_element("id", "kw")
time.sleep(3)
wk.send_keys("电影票房")

# print(page_source)
print(button.tag_name)
time.sleep(3)
button.click()
# 最新版的selenium执行完后会自动关闭浏览器
time.sleep(20)
browser.execute_script("")