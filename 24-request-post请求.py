"""
write: terence 
create date :2024/2/17 
"""
# https://fanyi.baidu.com/sug
import requests
import json

url = "https://fanyi.baidu.com/sug"
data = {
    "kw": "eye"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
}
# url 请求地址
# data 请求参数
# kwargs 字典
response = requests.post(url=url, data=data, headers=headers)
content = response.text
obj = json.loads(content)

print(obj)

# 总结
# post请求，是不需要编解码
# post请求的参数是data
# 不需要请求对象的定制
