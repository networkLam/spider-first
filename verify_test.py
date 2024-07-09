"""
write: terence 
create date :2024/2/26 
"""
import ddddocr
import requests
from bs4 import BeautifulSoup


# ocr = ddddocr.DdddOcr()
#
# with open("./verifycode.jpg","rb") as fp:
#     img_bytes = fp.read()
#     result = ocr.classification(img_bytes)
#     print(result)
# userAccount=2313202060431&userPassword=&RANDOMCODE=yxu3&encoded=MjMxMzIwMjA2MDQzMQ%3D%3D%25%25%25ZDEyMzQ%3D
#                                                                 A545671t45T30LY6L03k9O0C2Ju5kPAck8y2VOs
# https://jwxt.gdlgxy.edu.cn/jsxsd/xk/LoginToXk
# userAccount: 2313202060431
# userPassword:
# RANDOMCODE: yxu3
# encoded: MjMxMzIwMjA2MDQzMQ%3D%3D%25%25%25ZDEyMzQ%3D

# 解码学校登录密码的encoded字段
def Encoded(dataStr):
    scode = dataStr.split("#")[0]
    print(scode)
    sxh = dataStr.split("#")[1]
    print(sxh)
    code = "2313202060431" + "%%%" + "Axiaole@lin3"
    encoded = ""
    for item in range(len(code)):
        if item < 20:
            encoded = encoded + code[item:item + 1] + scode[0: int(sxh[item:item + 1])]
            scode = scode[int(sxh[item: item + 1]): len(scode)]
        else:
            encoded = encoded + code[item: len(code)]
            # item = len(code)
            break
    # print(encoded)
    return encoded
    pass


# Encoded('KRnswL0b5Tc58mTdX83bv2f2Fu07kCb59F98T0IaZ2G#33313322222211123322')
headers = {
'Connection':'keep-alive',
'Content-Length':'0',
'Cookie':'JSESSIONID=ECE806DF3719B0D00B926EE6541A7EBC; SERVERID=123',
'Origin':'https://jwxt.gdlgxy.edu.cn',
'Referer':'https://jwxt.gdlgxy.edu.cn/Logon.do?method=logon',
'Sec-Ch-Ua':'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}
session = requests.session()
# https://jwxt.gdlgxy.edu.cn/jsxsd/
# # 先获取网页
res_html = session.get("https://jwxt.gdlgxy.edu.cn/", headers=headers)
# print(res_html.text)
# 解析网页验证码
soup = BeautifulSoup(res_html.text, "lxml")
# 获取验证码
verify_code = soup.select("#SafeCodeImg")[0].attrs.get("src")
# verify_code = "https://jwxt.gdlgxy.edu.cn/jsxsd"+verify_code
verify_code = "https://jwxt.gdlgxy.edu.cn" + verify_code
# print(verify_code)
# 获得验证码的二进制数据
response_code = session.get(verify_code)
content_code = response_code.content
# 写入验证码以二进制方式
with open("code.jpg", "wb") as fp_code:
    fp_code.write(content_code)

# 解析验证码
ocr = ddddocr.DdddOcr()
# 读取验证码
with open("./code.jpg", "rb") as fp:
    img_bytes = fp.read()
    # 识别验证码
    code_result = ocr.classification(img_bytes)
    print("验证码是：" + code_result)
# 用于申请encoded
encoded_data = {
    'method': "logon",
    "flag": "sess"
}
# 申请encoded码
encoded_resource = session.post(url="https://jwxt.gdlgxy.edu.cn/Logon.do?method=logon&flag=sess", data=encoded_data, headers=headers)
print(encoded_resource.text)
print(encoded_resource.url)
# 改造encoded码
encoded_after_process = Encoded(encoded_resource.text)
print(f"改造后：{encoded_after_process}")

data = {
    'userAccount': '2313202060431',
    'userPassword': "Axiaole@lin3",
    # 验证码
    'RANDOMCODE': code_result,
    # encode
    "encoded": encoded_after_process
}
# https://jwxt.gdlgxy.edu.cn/Logon.do?method=logon
response = session.post(url="https://jwxt.gdlgxy.edu.cn/Logon.do?method=logon", headers=headers, data=data,
                        allow_redirects=True)
# print(response.text)
with open("home.html", "w", encoding="utf=8") as fp:
    fp.write(response.text)
# response = session.post(url="https://jwxt.gdlgxy.edu.cn/jsxsd/xk/LoginToXk",data=data,headers=headers)
# with open("home.html","w",encoding="utf=8") as fp:
#     fp.write(response.text)
