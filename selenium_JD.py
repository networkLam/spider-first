"""
write: terence 
create date :2024/5/6 
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
browser.get("https://p4psearch.1688.com/page.html?spm=a2638t.b_78128457.szyxdivertpopup.5.3836436cse4gAT&hpageId=old-sem-pc-list&cosite=baidujj_pz&keywords=%E6%89%8B%E6%9C%BA%E6%95%B0%E6%8D%AE%E7%BA%BF")
page_source = browser.page_source
with open("1688.html","w+",encoding="utf8") as fp:
    fp.write(page_source)
# text1 = browser.find_element(by=By.LINK_TEXT, value="hao123")
# print(text1.get_attribute("href"))
# get button element id value == su
# search_button = browser.find_element(By.CLASS_NAME, 'button')
# browser.execute_script("console.log('selenium!')")
# # wk = browser.find_element(By.ID,"kw")
# keyword = browser.find_element("id", "key")
# time.sleep(3)
# keyword.send_keys("手机")
#
# # print(page_source)
# print(search_button.tag_name)
# time.sleep(3)
# search_button.click()
# # 最新版的selenium执行完后会自动关闭浏览器
# time.sleep(20)
# browser.execute_script("")
# # 京东需要登录才能使用搜索
# # 先点击短信登录
# # sms-login
# msm = browser.find_element("id","sms-login")
# msm.click()
#
# # loginname 手机号
# phone = browser.find_element("id","mobile-number")
# phone.send_keys("17520666389")
# # nloginpwd 验证码
# sms_code = browser.find_element("id","sms-code")
# input_vife = input("请输入验证码：")
# sms_code.send_keys(input_vife)
#
# HTML = browser.page_source
# print(HTML)
