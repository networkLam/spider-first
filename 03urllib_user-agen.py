"""
write: terence 
create date :2024/1/21 
"""
import urllib.request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36"
}
url_address = "https://www.baidu.com"

request = urllib.request.Request(url=url_address, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf8")
print(content)
