person = {"name":"lam","age":25,"address":"YJ"}
# person['name'] = "jay"
# print(person['name'])
# # 通过dict .get 方式获取值更好
# # print(person.get("ll"))
# print(person.items())
# # 通过del 关键字删除一个属性
# del person['name']
# print(person.get("name"))
# print(person.values())
# person["de"] = "12138"
# print(person.values())
print(person)
del person["address"]
print(person)
print(person)
person.clear()
print(person)