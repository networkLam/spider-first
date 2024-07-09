"""
write: terence 
create date :2024/1/27 
"""
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
import urllib.request
import urllib.parse
from time import sleep


def create_request(page_index):
    url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data = {
        "cname": "阳江",
        "pid": "",
        "pageIndex": page_index,
        "pageSize": 10
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                      "Safari/537.36"
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(url=url, headers=headers, data=data)
    return request


def get_content(request: urllib.request.Request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(content)


if __name__ == '__main__':
    page_start = int(input("请输入起始页："))
    page_end = int(input("请输入终止页："))
    for page in range(page_start, page_end + 1):
        req = create_request(page)
        content = get_content(req)
        name = "KFC_LOCATION_"+str(page) + ".json"
        write_file(name,content)
        sleep(11)
