"""
write: terence 
create date :2024/5/6 
"""
import mysql.connector


class ConnectDataBase:

    def __init__(self):
        # 链接服务器（MySQL）
        self.conn = mysql.connector.connect(host='127.0.0.1', port=3306,
                                            user='root',
                                            passwd='root',
                                            db='electronic_commerce',
                                            charset='utf8')

    # 获取链接
    def get_Connect(self):
        return self.conn

    # 关闭链接
    def close_Connect(self):
        self.conn.close()


conn = mysql.connector.connect(host='127.0.0.1', port=3306,
                                            user='root',
                                            passwd='root',
                                            db='electronic_commerce',
                                            charset='utf8')
# 光标
cursor = conn.cursor()
query1 = "select * from user"
query2 = "select * from user where gender = %s"
# cursor.execute(query2,['男'])
cursor.execute("insert into product(price,state,p_describe,picture_name) values(%s,%s,%s,%s)",('1999','1','unknown','1.jpg'))
# 对数据有修改的要提交修改
print(cursor.lastrowid)
conn.commit()
# result = cursor.fetchall()
# print(result)
# cursor.close()

# C_DB = ConnectDataBase()
# cursor = C_DB.get_Connect().cursor()
# cursor.execute("insert into product(price,state,p_describe,picture_name) values(%s,%s,%s,%s)",['1998','1','unknown','1.jpg'])
# result = cursor.fetchall()
# print(result)
# cursor.execute("select * from user where uid = 2")
# result = cursor.fetchall()
# print(result)
# C_DB.close_Connect()
