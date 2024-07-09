"""
write: terence 
create date :2024/1/20 
"""
import urllib.request

# (1) 使用urllib获取百度数据
url = "http://www.baidu.com"
# (2)模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
print(response)
print("-----------------")
# (3)获取相应中的页面中的源码
# read方法返回的是二进制数据
# 将二进制转换成字符串
# 二进制-->字符串 解码decode
content = response.read().decode('utf-8')
# (4)打印数据
print(content)

