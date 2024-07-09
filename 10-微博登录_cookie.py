"""
write: terence 
create date :2024/1/29 
"""
#SINAGLOBAL=5294870502360.66.1682938209645; SCF=Anveleg4KsdaBZCU5EBJc4b378wB9s4j3Ty2b7FqaVWJAkfva5BZj3rCQfWdRjGIxay0PBBygForh1TBGgaHhTQ.; UOR=,,www.baidu.com; ULV=1705502840536:12:1:1:4760425265947.541.1705502840531:1703848890149; ALF=1709092275; SUB=_2A25Is1DjDeRhGeBJ41YQ-S3LyzSIHXVrsewrrDV8PUJbkNANLWaskW1NRiGIiZQ4xHjLBEmJcdPhHBHNWr00OW2E; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhDI1WAhadN5F07aMKko3gT5JpX5KMhUgL.FoqN1hBp1KeNehn2dJLoI0YLxKMLB.2LB-qLxKML1h.L1-zLxK-LBK-LBoqLxKBLBonL12BLxKnLBKqL1h2LxK-L122LBK5LxKnLB.-LBKet; WBPSESS=oXBwrbaayT6eQYo2MwbVFwiW6uDyxamntKHscfBbhSP7MMdviWCh97peD4Oy2L5ALO7Nlj19daiFwUCdaaQeS50IHAdi2LNcEIuCz77z4pnzcuM7qIRiLhsljc9tOGyjHTiNRgPhkSz921hgVzk8wA==; XSRF-TOKEN=Ohz3x7WIu_CAmMK1Z3odtDaA
import urllib.request
import urllib.parse

url = "https://weibo.com/ajax/profile/info?uid=6784193708"

headers = {
    # ":authority": "weibo.com",
    # ":method": "GET",
    # ":path": "/",
    # ":scheme": "https",
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cache-Control": "no-cache",
    'Cookie':"SINAGLOBAL=5294870502360.66.1682938209645; SCF=Anveleg4KsdaBZCU5EBJc4b378wB9s4j3Ty2b7FqaVWJAkfva5BZj3rCQfWdRjGIxay0PBBygForh1TBGgaHhTQ.; ALF=1709092275; SUB=_2A25Is1DjDeRhGeBJ41YQ-S3LyzSIHXVrsewrrDV8PUJbkNANLWaskW1NRiGIiZQ4xHjLBEmJcdPhHBHNWr00OW2E; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhDI1WAhadN5F07aMKko3gT5JpX5KMhUgL.FoqN1hBp1KeNehn2dJLoI0YLxKMLB.2LB-qLxKML1h.L1-zLxK-LBK-LBoqLxKBLBonL12BLxKnLBKqL1h2LxK-L122LBK5LxKnLB.-LBKet; XSRF-TOKEN=texNLPtixJUmHZqFGFeRnqI_; WBPSESS=oXBwrbaayT6eQYo2MwbVFwiW6uDyxamntKHscfBbhSP7MMdviWCh97peD4Oy2L5ALO7Nlj19daiFwUCdaaQeS6buuyu-OF-kiIMdTtM3XVAlNy9c40tvD57n_gmFsh6WbRRyXK93g3cWszbVANMSfw==; _s_tentry=localhost:63342; UOR=,,localhost:63342; Apache=500204261435.2531.1706540610646; ULV=1706540610788:13:2:1:500204261435.2531.1706540610646:1705502840536",
    # "Pragma": "no-cache",
    # "Referer": "https://www.baidu.com/",
    # "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    # "Sec-Ch-Ua-Mobile": "?0",
    # "Sec-Ch-Ua-Platform": "Windows",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "same-origin",
    # "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(response)
print(content)

