"""
write: terence 
create date :2024/2/3 
"""
import urllib.request
import json
import jsonpath

# url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1706948649028_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true"
# # 定制请求头
# headers = {
#     'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
#     # 'Accept-Encoding':'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Bx-V': '2.5.10',
#     'Cookie': 'thw=cn; cna=D+L5HPRtTF4BASQJiVrKGCTe; tracknick=%5Cu9189%5Cu9152%5Cu4F24%5Cu4EBA%5Cu79BB; l=fBIoKc8qNhdRPvU1BOfahurza77ThIRbMuPzaNbMi9fPOp5HJeWNW1eB9PYMCnGVEsUMR3RxBjFXBVT3RPUsgxv9-eTCgsDKndLnwpzHU; lgc=%5Cu9189%5Cu9152%5Cu4F24%5Cu4EBA%5Cu79BB; miid=152485632394667510; t=5d1832d459b6a4f8cf134953e056510f; 3PcFlag=1706415660039; sgcookie=E100LxFmxKDmwQWMRZNxWmtUJMfVBdDYT8ty7QjlgqIpSa%2FtWgWFwzaW1ahs41yJDs%2FQgGAEKdv4nX4prWp1qM4zkv7TncRnl8TiEzPzTrjuNbUHvDmBVj5yarS%2Fnyw3dQrd; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&nk2=tPJoLtzuiCwfxw%3D%3D&id2=UUwVYDAjwGWuHA%3D%3D&vt3=F8dD3CmZlJNZioiFs6U%3D; uc4=nk4=0%40thQZB0nDwhtVByqi3ndbqgzospoe&id4=0%40U27KDBC%2Byxna2JLVMEDTUKeZ3me8; _cc_=V32FPkk%2Fhw%3D%3D; xlly_s=1; tb_city=441700; tb_cityName="0fS9rQ=="; cookie2=15bc0d74eb830b356b89106891b09a48; v=0; _tb_token_=e3eeee3678a05; tfstk=e5dp3_jDJcmhm6rVIXHMaLBzdt0inBLE-H8bZgj3FhK90H3FEJvHeuI9l2SnUv-JB3tNKMOJz7QWP3uFq2kM8e5PNmmDwjYe8__KQ2h0CeF2d_immf2g59ohNpD_ipsxKWaZMqFeTQQIhBxQkG44awWdcFH4N73h7ojvRSV0gCCApiiGX7NW6wszTIAx8BEcDa2IWVezU9_aq4OSMn9DbjbOmV2gU8WG7NImWVezU9_NWi0ii8yPIN5..; isg=BBsbLf4r-h_hHQcBp-1eUJsRqn-F8C_y9pIOYw1bjJox7DrOlcUpQxgihkziFIfq',
#     'Referer':'https://dianying.taobao.com/',
#     'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Windows"',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
# }
# # 定制请求头
# request = urllib.request.Request(url=url, headers=headers)
# # 发起网络请求
# response = urllib.request.urlopen(request)
# # 解析内容
# content = response.read().decode("utf-8")
#
# # 去掉奇怪的前缀jsonp109(
# content = content.split("(")[1].split(")")[0]
# print(content)
#
# # 写入内容
# with open("taopiaopiao.json", "w", encoding="utf-8") as fp:
#     fp.write(content)

# 解析json文件 take out regionName
obj = json.load(open("taopiaopiao.json","r",encoding="utf-8"))
# 通过格式take out
city_list = jsonpath.jsonpath(obj,"$.returnValue..regionName")
print(city_list)
