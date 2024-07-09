"""
write: terence 
create date :2024/2/1 
"""
# //*[@id="su"]
import urllib.request
from lxml import etree

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36"
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
# print(content)
tree = etree.HTML(content)
# come to tree take out value
result = tree.xpath("//*[@id='su']/@value")
print(result)



