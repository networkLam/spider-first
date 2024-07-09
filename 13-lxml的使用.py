"""
write: terence 
create date :2024/2/1 
"""
from lxml import etree
# xpath解析
# （1）本地文件 etree.parse
# （2）服务器响应的数据 response.read().decode("utf-8") etree.HTML()
# xpath解析本地文件
tree = etree.parse("citylist.html")
print(tree)

# text()是解析当前的get到的文本
# li_list = tree.xpath('//ul/li/text()')
# use tag[@attribute] get li tag beneath ul and li attribute id equal to location
# li_list = tree.xpath('//ul/li[@id="location"]/text()')
# get ul tag include attribute class
# li_list = tree.xpath('//ul/li[@class]/text()')
# get ul tag id equal to c3  and then get class value
# li_list = tree.xpath('//ul/li[@id="c3"]/@class')
#  contains
# li_list = tree.xpath('//ul/li[contains(@id,"c")]/text()')
# query statr-with char someone
li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')
print(f"total {len(li_list)}")
print(li_list)
