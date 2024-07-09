"""
write: terence 
create date :2024/5/7 
"""
# from lxml import etree
# tree = etree.parse("1688.html")
# print(tree)
from lxml import etree
import urllib.request
import unit_next_layer
from database_connect_code import ConnectDataBase

# xpath解析
# （1）本地文件 etree.parse
# （2）服务器响应的数据 response.read().decode("utf-8") etree.HTML()
# xpath解析本地文件
# when not is standard  HTML , must add parser parameter.
# 当HTML不规范时需要补充个API tips：lxml.etree.XMLSyntaxError
parser = etree.HTMLParser(encoding="utf8")
tree = etree.parse("1688.html", parser=parser)
# main picture ,just mini picture
main_picture = tree.xpath("//div[@class='mainPic']//img/@src")
print(f"len is {len(main_picture)}")
print(main_picture)
# //span[@class='subject'] 产品标题
product_name = tree.xpath("//span[@class='subject']/@title")
print(f"len is {len(product_name)}")
print(product_name)
# //span[@class='price_num'] get product price
product_price = tree.xpath("//span[@class='price_num']/text()")
print(f"len is {len(product_price)}")
print(product_price)
# next layer link
link = tree.xpath("//div[@class='smart_ui_offer offer_item']/a/@href")
print(f" link len is {len(link)}")
print(link[0])
# need to product price process ,because original data is divide Yuan and Fen.
# 10分 = 1角 1元 = 100分
list_price = []
index = 0
while True:
    # print("before", product_price[index] + product_price[index + 1])
    temp = round((float(product_price[index] + product_price[index + 1]) * 100), 2)
    # print("after", temp)
    list_price.append(temp)
    index = index + 2
    if index >= len(product_price):
        break

print(list_price)
# print(tree)
# 链接数据
DB = ConnectDataBase()
cursor = DB.get_Connect().cursor()
# 插入数据
sql = "insert into product(price,state,p_describe,picture_name) values(%s,%s,%s,%s)"
# cursor.execute("select * from user")
# result = cursor.fetchall()
# print(result)
for item in range(len(main_picture)):
    # 名字
    name = product_name[item]
    # 价格
    price = list_price[item]
    # 给图片起个名字
    res = main_picture[item].split("/")
    pic_name = res[len(res) - 1]
    # 下载图片
    urllib.request.urlretrieve(main_picture[item], './productPic/' + pic_name + ".jpg")
    # 执行插入语句
    cursor.execute(sql, (price, "1", name, pic_name))
    # 获取插入的主键
    primary_key = cursor.lastrowid
    content = unit_next_layer.get_data(link[item])
    # 找到图片链接
    a_picture = etree.HTML(content)
    content_src = a_picture.xpath("//img[@class='detail-gallery-img']/@src")
    # 图片命名
    res = content_src[item].split("/")
    details_picture_name = res[len(res) - 1]

#     提交修改
    DB.get_Connect().commit()
