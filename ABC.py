import os

# 先假设T为1，则只需要输入一组测试用例
T = int(input("input T:"))

# 输入所有测试用例
for i in range(T):
    # list.i = input().split(" ")
    # print(list.i)
    list[i] = input()

# 测试用例列表转换为int型数据

# 进行A+B>C的判断

# 输出：根据i in range（T）来进行输出


xlist = list.split(" ")
xlist = [int(xlist[i]) for i in range(len(xlist))]

if xlist[0] + xlist[1] > xlist[2]:
    x_tag = 'true'
else:
    x_tag = 'false'

for i in range(T):
    print("case i:", x_tag)
