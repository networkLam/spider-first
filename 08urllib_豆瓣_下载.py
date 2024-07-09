"""
write: terence 
create date :2024/1/27 
"""
# url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20"
# 先整理URL
import urllib.request
import urllib.parse
from time import sleep


def create_url(page_num):
    base_url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&"
    data = {
        "start": (page_num - 1) * 20,
        "limit": 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                      "Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=headers)
    return req


def get_content(req):
    response = urllib.request.urlopen(req)
    _content = response.read().decode("utf-8")
    print("getting...")
    return _content


def write_content(file_name, con):
    with open(file_name, "w", encoding="utf-8") as fp:
        fp.write(con)
        print("write finish.")


if __name__ == '__main__':
    page_start = int(input("请输入起始页："))
    page_end = int(input("请输入终止页："))
    for page in range(page_start, page_end + 1):
        request = create_url(page)
        content = get_content(request)
        filename = "douban_" + str(page) + "_page.json"
        write_content(filename, content)
        sleep(10)
