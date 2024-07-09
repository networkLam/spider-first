"""
write: terence 
create date :2024/2/3 
"""
# attribute,attitude,altitude
# 属性 ， 态度、看法  ， 海拔、高度
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("18-beautiful-study.html", "r", encoding="utf-8"), "lxml")
# print(soup.a)
# print(soup.a.attrs)
# 返回第一个被找到的a标签
# print(soup.find("a"))
# 指定any tag the attribute ,  return  entire tag info
# print(soup.find("a", title="google"))
# keyword the used
# print(soup.find("a", class_="search"))
# return is list ,within has you appoint the HTML tag
# 如果想要获取的是多个标签，那么需要再find——all的参数中添加的是列表的数据
# print(soup.find_all("a"))
# print(soup.find_all("li",limit=4))
# select all a tag
# 推荐使用select选择器 而不是find
# print(soup.select("a"))
# select with class attribute ,name is "search" （类选择器
# print(soup.select('.search'))
# id select (id 选择器
# print(soup.select("#su"))
# print(soup.select('ul>li[id="l1"]'))
# attribute selected （属性选择器
# li tag with id attribute
# print(soup.select("li[id]"))
#  found id equal 'l2'  within all li tag
# print(soup.select("li[id='l2']"))
# 层级选择器
# 后代选择器
# print(soup.select("div li"))
# 子代选择器
# 某标签的第一级子标签
# 注意：很多的计算机编程语言中，如果不加空格不会输出内容，但是在bs4中会报错
# print(soup.select("div > ul> li"))
# 找到a标签和li标签的所有对象
# print(soup.select("a,li"))
# print(soup.select("a,li")[0].string)
# print(soup.select("a,li")[0].get_text())  # 获取标签中的文本信息
# print(soup.select("a,li")[0].name)  # 返回的是标签的名称
# print(soup.select("a,li")[len(soup.select("a,li")) - 1].attrs.get('title')) # 返回的是指定属性的值
# obj = soup.select("#d1")
# 如果标签对象中只有内容，那么string和get_text()都能获取到内容
# 如果标签中还有标签那么string就不能获取到内容，get_text()能获取到
# print(obj[0].string)
# print(obj[0].get_text())
# 获取节点的属性
obj = soup.select(".search")
print(obj)
# print(obj.name)  # 获取标签的名字
# print(obj.attrs)  # 将标签中的属性打包为字典类型返回
# print(obj.attrs.get("title"))  # 获取标签中属性的值
