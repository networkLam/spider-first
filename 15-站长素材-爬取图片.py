"""
write: terence 
create date :2024/2/1 
"""

# https://a2put.chinaz.com/slot/callback?id=s1694629161422034&fromUrl=https://sc.chinaz.com/tupian/xiaomaotupian.html
# https://a2put.chinaz.com/slot/callback?id=s1694629161422034&fromUrl=https://sc.chinaz.com/tupian/xiaomaotupian_2.html
# https://a2put.chinaz.com/slot/callback?id=s1694629161422034&fromUrl=https://sc.chinaz.com/tupian/xiaomaotupian_3.html
# https://sc.chinaz.com/tupian/xiaomaotupian.html
# https://sc.chinaz.com/tupian/xiaomaotupian_2.html
# https://sc.chinaz.com/tupian/xiaomaotupian_3.html
import urllib.request
import urllib.parse
from lxml import etree


# generate 1 to 10 page url
def create_url(num: int):
    base_url = "https://sc.chinaz.com/tupian/xiaomaotupian"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                      "Safari/537.36"
    }
    link = ".html" if num == 1 else "_" + str(num) + ".html"
    url = base_url + link
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(req: urllib.request.Request):
    response = urllib.request.urlopen(req)
    content = response.read().decode("utf-8")
    # print(content)
    tree = etree.HTML(content)
    # 一般图片的网站都会进行懒加载 需要确定src的链接
    result = tree.xpath("//img[@class='lazy']/@data-original")
    # print(result)
    # 解析
    photos_name = tree.xpath("//img[@class='lazy']/@alt")
    print(photos_name)
    length = len(result)
    print(length)
    if length != 0:
        for item in range(length):
            url_header = "https:"
            entirely = url_header + result[item]
            urllib.request.urlretrieve(entirely, "./photos/" + photos_name[item] + ".jpg")
    else:
        print("result为空，请检查")
    # 使用xpath解析当前页面有多少个Img标签


# for page in range(1, 11):
#     create_url(page)
get_content(create_url(1))
