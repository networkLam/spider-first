"""
write: terence 
create date :2024/5/7 
"""
import urllib.request
from lxml import etree


def get_data(src):
    res = urllib.request.urlopen(url=src)
    content = res.read().decode('utf8')
    # with open("details.html", "w+",encoding="utf8") as fp:
    #     fp.write(content)
    return content


parser = etree.HTMLParser(encoding="utf8")
content_HTML = get_data(
    "https://dj.1688.com/ci_bb?a=1309083318&e=g9ZnxX0mqEj1S3jrrDaIvk0hDBqE5gO6TokOO5VdVDb-yVPpR0o-F-6ODpyyk3fEnkX53HeSI7xHPqMu2T7MeWSvSEYZVWWp.zwJdmdgyVDaows8dzmE-JmyplNZs6.6jgLWLP4aMetEVX00WkPFKRwGE8gf4TEJfRtk8E8tximUyu0edQ6G542gQu3H7tzV7gmQ1zBR2Bc7SU02RS050Hiu9V5z95hnD.PCJNQaIP.GmLG1nH8ogAxM7rUrHU8Vy77dTRxMxP027E4qBNrh0JT8qve.vKoK-YeLGbJzQ4TgDyQRBzHffEpxGkNo4q9ANpEKAS3kaToFZtZorDTsgL6Q0viupUOaTvto6Rpjaokz754FAK42JuA-ggZ71ekuXXLuKO2tMMQ9nKzsHmsdBLzcTTZQqKJpjxWgpm40RhaQpmK5JYXaSZLcL82wLnjCX03wqzV0hD2hB--fdgrJSKmGcZ.TsR9.N5Hmw9o9IGIQjPzXguJdUo-BRfCGlC543WniXwaa5xxfX6w6Sgt084wMnnWxRC9EKyKzGk7rbXqU9sg.VB1ew0ZJxihj4V7YZSg1otdyI7ELLC9UnyGBwzEUxZ75JSOVHIgFd0miDzFgjxsFDcmgbvtURl3CBKXl8aj2BfC.xJdhZY.PExAdoUPmAdG8zWr5D7L9WGzYJko8exyFe-4KIDASmJTgHiTNb8eMaHu.H5Sy0YkwltYBzTZPknxHUvwqlL1rs77toG5WiplMT7rL3Z3assfJU9w4hKpS4fpAwXcebCtv3aCk9vcIscYAU8vmjE1OCt5DffkoLSIKH1yPvMpslgZSOAsJDTYkq20BisiHi9yrjtKu5uaO7mBDRFE0VPIuy-bYixiYlu1-6P0yDrj1wBrDC-3zwyaL55BrDxeW9PUAe67CcyEJx6LSmQgIKXAXXBGRRiKxicsRiXyMDfQB7z5TK84iWIO5T--xcI4tdgYD.mqLhm4yyFgYcYgNA4vpEci0luTYPaTviqh.8FcUwjtWNVDIWmsjmZqMO8l.ccPQAD5U-McAnjiTchvIT6AAuN-9jbfxtSu1i8QRRZOVo0s.LteNU22ykFQFwiicZqUx1AH38zXcZiBgCFTHShBw02Q6tVV2SnIqA5UkupUSQfyyqXmd--tnHjO1kfGn-2b-oI3N9dzOK4kdyymwHUnWAF5TtRNYgCPOWRPV8z2sseCSbhBXMKfBiowb3xqvDXQa6NOFlaBA6WmGMyqewTDFOvp66764pOdT5Wvgh94o27UtZj8LdbjDNKXXo7Q2jDES1NAxJID4VhvoZCnpIxaPpyM04FMTElgmazaqDPXZ9T-5U9ml&v=4&ap=1&rp=1")
tree = etree.HTML(content_HTML,parser=parser)
print(content_HTML)
picture_src = tree.xpath("//img[@class='detail-gallery-img']/@src")
print(picture_src)
"""
固定二级域名 /店铺ID.html?+商品id
https://detail.1688.com/offer/718152613503.html?pid=301011_0000&ptid=&exp=enquiry%3AB%3Bxlyx%3AB&cosite=baidujj_pz&tracelog=p4p&_p_isad=1&clickid=f67b8f3d98414edbbb454ae026ae70a2&sessionid=cdd4944f8c53d8acd2d2015406577f22&a=1568&e=WGXoQbeijcHETFOTY8XkCsV-DmgUzVBXxvjJ08yn3DQBCySPVdYkofhgaxoCrJd6u6ssQ-XBKcJ6vkjjnEwxbIfoKz9-xBNTxJ-kyMv-XLE6pIdLG2ErXNvXKl19xYp2NzSDJXJE--zdGBrMOru35uOU1wqRbDYYBBwPyUys-KOMa4Ofj4o5nXcm-HPMlslzj92bxcYgz1H-5OWYygqRc0TRy38rwIzImLiKZP5TKQ7Diakgy843T8zNj-f7O8T4fje-v4YYav-rEW8TvKkbI.Ph8C5M2nhh&sk=sem&style=1
"1081181309881": {
                        "componentType": "@ali/tdmod-pc-od-main-pic",
                        "data": {
                            "offerImgList": ["https://cbu01.alicdn.com/img/ibank/O1CN01fc8pjr25B6BUQLFGE_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN01kBB0ut25B6BRc0FvF_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN01PH2c1L25B6BWLB76V_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN01R5zsXm25B6BQSADsB_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN019rb6Qd25B6BWLNKhH_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN01fc8pjr25B6BUQLFGE_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN01fc8pjr25B6BUQLFGE_!!2897747487-0-cib.jpg", "https://cbu01.alicdn.com/img/ibank/O1CN01fc8pjr25B6BUQLFGE_!!2897747487-0-cib.jpg"],
                            "video": {
                                "coverUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01oK4ioq1Bs2q8pQyLS_!!0-0-cib.jpg",
                                "videoId": 409820053660,
                                "state": 6,
                                "title": "双Type-c头PD数据线传输公对公适用华为小米三星笔记本快充数据线",
                                "videoUrl": "https://cloud.video.taobao.com/play/u/2897747487/p/2/e/6/t/1/409820053660.mp4"
                            },
                            "canShowAllImage": true,
                            "isBestOffer": true,
                            "isBestOfferUrl": "https://img.alicdn.com/tfs/TB1ZwSvqG6qK1RjSZFmXXX0PFXa-100-100.png",
                            "offerId": 718152613503,
                            "subject": "双Type-c头PD数据传输公对公适用华为小米三星笔记本快充数据线"
                        }
                    },

"""