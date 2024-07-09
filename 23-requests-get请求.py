"""
write: terence 
create date :2024/2/17 
"""
import requests

url = "https://www.baidu.com/s?"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
}
data = {
    "wd": "广州"
}
# parameter 参数
response = requests.get(url=url, headers=headers, params=data)
content = response.text
print(content)
#url 请求路径资源
# 参数使用params
# 参数无需urlencode编码
# 请求资源路径中的？可以加可以不加
