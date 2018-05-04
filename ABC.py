import os

# 先假设T为1，则只需要输入一组测试用例,X从1开始
T = int(input("input T:"))

# 输入多组时使用字典
dic = { }
dict = { }
# 输入所有测试用例
for i in range(1, T+1):
    # list.i = input().split(" ")
    # print(list.i)
    # list[i] = input()
    # print(list[i])
    dic[i] = input().split(":")
    # dict[i] = dic[i].split(":")
    xlist = (','.join(dic[i])).split(" ")
    xlist = [int(xlist[i]) for i in range(len(xlist))]
    if xlist[0] + xlist[1] > xlist[2]:
        x_tag = 'true'
    else:
        x_tag = 'false'
    print("case #%d:"%i, "%s"%x_tag)
    # arr = list(map(int,xlist))
    # print(arr)

# 测试用例列表转换为int型数据
# xlist = list.split(" ")
# xlist = [int(xlist[i]) for i in range(len(xlist))]
# list = [int(dic[i]) for i in range(len(dic))]



# 进行A+B>C的判断
# if xlist[0] + xlist[1] > xlist[2]:
#     x_tag = 'true'
# else:
#     x_tag = 'false'

# 输出：根据i in range（T）来进行输出


# for i in range(T):
#     print("case i:", x_tag)
