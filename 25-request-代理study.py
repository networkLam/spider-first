"""
write: terence 
create date :2024/2/17 
"""
import requests

url = "http://www.baidu.com/s?"
data = {
    "wd": "ip"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
}
# use ip proxy
proxy = {
    "http": "your ip"
}
response = requests.get(url=url, headers=headers, proxies=proxy)
content = response.text
with open("baidu_ip.html", "w", encoding="utf-8") as fp:
    fp.write(content)
