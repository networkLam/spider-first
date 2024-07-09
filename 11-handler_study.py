"""
write: terence 
create date :2024/1/30 
"""
import urllib.request
import urllib.parse

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
   }
request = urllib.request.Request(url=url,headers=headers)
# 创建handle对象
handler = urllib.request.HTTPHandler()
# 获取opener对象
opener = urllib.request.build_opener(handler)
# 调用opener中的open方法
response = opener.open(request)
content = response.read().decode("utf-8")
print(content)
