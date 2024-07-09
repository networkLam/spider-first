"""
write: terence 
create date :2024/1/22 
"""
import urllib.request
import urllib.parse
import json
url_add = "https://fanyi.baidu.com/sug"
data = {
    "kw": "hello"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36"
}
# 先转码 转成byte类型
data = urllib.parse.urlencode(data).encode("utf-8")
# 定制请求对象
request = urllib.request.Request(url_add, data=data, headers=headers)
# 像地址发送请求
response = urllib.request.urlopen(request)
# 解析请求
content = response.read().decode("utf-8")
# 将请求解析为字典类型
result = json.loads(content)
print(result)
