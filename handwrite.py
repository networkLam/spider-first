"""
write: terence 
create date :2024/2/6 
"""


# 打印i到j使用递归的方式
# 递归的三个重要条件
# 找重复
# 找变化
# 找边界
def iTOj(i, j):
    if i > j:
        return
    print(i)
    iTOj(i + 1, j)


# iTOj(1, 5)

# 使用递归写阶乘
def jiecheng(n):
    if n <= 1:
        return 1
    return jiecheng(n - 1) * n


print(jiecheng(7))


# 使用循环写阶乘

def for_jiecheng(n):
    total = 1
    for item in range(1, n + 1):
        total = total * item
    return total


print(for_jiecheng(7))