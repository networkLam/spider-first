"""
write: terence 
create date :2024/1/24
describe 获取豆瓣电影的20条数据
"""
import urllib.request
import json
from time import sleep


# url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20"
# # start 标识起始位
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
#                   "Safari/537.36"
# }
#
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode("utf-8")
# print(content)
# # 将数据写入file
# with open("douban.json", "w", encoding="utf-8") as fp:
#     fp.write(content)


def get_doubanData(num, filename: str):
    url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=" + str(
        num) + "&limit=20"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                      "Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    with open(filename, "a+", encoding="utf-8") as fp:
        fp.write(content)
    pass


# sleep 是阻塞的
#
# for i in range(0, 3):
#     get_doubanData(i * 20, "douban1.json")
#     sleep(10)
get_doubanData(0,"douban2.json")
# for i in range(3 ):
#     print(i)
#     sleep(10)
