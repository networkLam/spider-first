"""
write: terence 
create date :2024/2/15 
"""
# https://active.starbucks.com.cn/sortable/2548e2f1-4fe3-4bed-8317-acf289659278.jpg

import urllib.request
from bs4 import BeautifulSoup
import re

# url = "https://www.starbucks.com.cn/menu/"
# response = urllib.request.urlopen(url)
# content = response.read().decode("utf-8")
# urllib.request.urlretrieve("https://www.starbucks.com.cn/menu/","./html/starbucks.html")


soup = BeautifulSoup(open("./html/starbucks.html", "r", encoding="utf-8"), "lxml")
# print(soup)
content = soup.select("div[class='wrapper fluid margin page-menu-list']> ul > li")
# print(len(content))
# print(content[0].select("strong")[0].get_text())
image_base_url = "https://www.starbucks.com.cn"
text = 'background-image: url("/images/products/affogato.jpg")'
pattern = r'url\("([^"]+)"\)'
for item in range(len(content)):
    url = content[item].select("div")[0].attrs.get("style")  # 获取style属性的值
    production_name = content[item].select("strong")[0].get_text() # 获取产品的名字
    match = re.search(pattern, url)  # 进行正则匹配获取URL中的内容
    if match:
        url = image_base_url + match.group(1)
    print(url)
    print(production_name)

# match = re.search(pattern, text)
# if match:
#     url = match.group(1)
#     print(url)  # 输出: /images/products/affogato.jpg
