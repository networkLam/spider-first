"""
write: terence 
create date :2024/5/6 
"""
# 爬取京东网站的数据
import requests
from lxml import etree

url = "https://p4psearch.1688.com/page.html?spm=a2638t.b_78128457.szyxdivertpopup.6.3836436cse4gAT&hpageId=old-sem-pc-list&cosite=baidujj_pz&keywords=%E8%BF%B7%E4%BD%A0%E8%87%AA%E6%8B%8D%E6%9D%86"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36"
    }
res = requests.get(url=url,headers=headers)
res.encoding = "utf-8"
content = res.text
print(res.text)
with open("1688.html","w+",encoding="utf8") as fp:
    fp.write(content)
# tree = etree.parse("JD.html",etree.HTMLParser())
# print(tree)
# list1 = tree.xpath("//div[@class='p-img']//img/@src")
# //div[@class='p-name p-name-type-2']//em
# list1 = tree.xpath("//div[@class='p-name p-name-type-2']//em/text()")
# print(f"total is {len(list1)}")
# print(list1)
#                                                                       b1ad95c27d642433.jpg.avif
#        img11.360buyimg.com/n7/jfs/t1/128027/35/41911/68156/6638974cFba9bd3e2/b1ad95c27d642433.jpg.avif
#https://img13.360buyimg.com/n7/jfs/t1/247390/4/8349/62875/6630ba90Fca4175ad/188cb1ef3a579bb9.jpg.avif