"""
write: terence 
create date :2024/2/1 
"""

import json
import jsonpath

obj = json.load(open("./store.json", "r", encoding="utf-8"))
# get book author
author_list = jsonpath.jsonpath(obj,"$.store.book[*].author")
# get store all author
store_all_author = jsonpath.jsonpath(obj,"$.store..author")
# get all data beneath store
store_all_data = jsonpath.jsonpath(obj,"$.store.*")
# get  price data beneath store
store_all_price = jsonpath.jsonpath(obj,"$.store..price")
# get data within all author
data_all_author = jsonpath.jsonpath(obj,"$..author")

# take out contain book within include isbn keyword
data_include_isbn = jsonpath.jsonpath(obj,"$..book[?(@.isbn)]")
# print(data_include_isbn)
# take out 10 price of greate then
data_greate_then_ten = jsonpath.jsonpath(obj,"$..book[?(@.price>10)]")
print(data_greate_then_ten)
# print(author_list)
# obj = json.load(open("./douban_1_page.json", "r", encoding="utf-8"))
# # $ 符表示根目录  *表示当前目录下的所有子项
# author_list = jsonpath.jsonpath(obj,"$.[*].title")
# # print(obj)
# print(author_list)
