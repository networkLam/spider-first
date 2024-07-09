"""
write: terence 
create date :2024/1/21 
"""
import urllib.request
# 下载一个网页
# url_page = "http://www.baidu.com"
# urllib.request.urlretrieve(url_page,"baidu.html")
# print("finish")
# 下载一张图片
url_img = "https://img0.baidu.com/it/u=1274159762,1426162804&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=582"
urllib.request.urlretrieve(url_img,"./photos/lisa2.jpg")
print("finish")