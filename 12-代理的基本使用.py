"""
write: terence 
create date :2024/2/1 
"""
import urllib.request

url = "http://www.baidu.com/s?wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
}
# 定制请求头
request = urllib.request.Request(url=url, headers=headers)

# handler = urllib.request.HTTPHandler()
# opener = urllib.request.build_opener(handler)
proxies = {
    "http": "47.120.35.50"
}
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
# response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")
print(response)
print("------------------------------")
print(content)
with open("myIp2.html", "w", encoding="utf-8") as fp:
    fp.write(content)
