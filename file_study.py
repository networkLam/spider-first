"""
write: terence 
create date :2024/1/20 
"""
import os
import json
# fw = open(os.getcwd() + "/test.txt", "w")
# fw.write("this test\n"* 5)
# fw.close()
# fr = open(os.getcwd() + "/test.txt","r")
# for item in fr.readlines():
#     print(item)
#
# fr.close()
# print(__name__)
# print(os.getcwd())
# fw = open(os.getcwd() + "/test.txt", "w")
# person = { "name" : "lam","age" : "25","address": "YJ"}
# fw.write(json.dumps(person))

fr = open(os.getcwd() + "/test.txt","r")
content = fr.readline()
# print(type(content))
# json.dump(content)
# print(person)
person = json.loads(content)
print(person)
print(person["name"])