"""
write: terence 
create date :2024/2/16 
"""
import requests

url = "http://www.baidu.com"
response = requests.get(url=url)
# 一个类型和六个属性
# <class 'requests.models.Response'>
print(type(response))
# 设置响应的编码格式
response.encoding = "utf-8"
# 返回网页源码
# print(response.text)
# 返回url地址
print(response.url)
# 返回的是二进制文件
# print(response.content)
# 返回响应的状态码
print(response.status_code)
# 返回响应头
print(response.headers)
