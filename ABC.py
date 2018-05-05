"""给定区间[-2的31次方, 2的31次方]内的3个整数A、B和C，请判断A+B是否大于C。
输入描述:
输入第1行给出正整数T(<=10)，是测试用例的个数。随后给出T组测试用例，每组占一行，顺序给出A、B和C。整数间以空格分隔。

输出描述:
对每组测试用例，在一行中输出“Case #X: true”如果A+B>C，否则输出“Case #X: false”，其中X是测试用例的编号（从1开始）。
示例1
输入

4
1 2 3
2 3 4
2147483647 0 2147483646
0 -2147483648 -2147483647
输出
Case #1: false
Case #2: true
Case #3: true
Case #4: false"""


# 先假设T为1，则只需要输入一组测试用例,X从1开始
T = int(input())

# 输入多组时使用字典
dic = { }
list_tag = []
arr = []
# 输入所有测试用例
for i in range(T):
    # list.i = input().split(" ")
    # print(list.i)
    dic[i] = input().split(":")
    # dict[i] = dic[i].split(":")
    xlist = (','.join(dic[i])).split(" ")
    xlist = [int(xlist[i]) for i in range(len(xlist))]
    if xlist[0] + xlist[1] > xlist[2]:
        list_tag.append('true')
    else:
        list_tag.append('false')

for i in range(len(list_tag)):
    arr += ['case #', str(i), ':', list_tag[i], '\n']
print(''.join(arr))
# for i in range(len(list_tag)):
#     print("case #%d:"%(i+1), "%s"%list_tag[i])

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
