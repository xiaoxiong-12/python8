#!/usr/bin/python
# author Yu
# 2023年06月08日
list1 = [1, 5, 7, 2, 4, 5, 2, 5, 5, 5, 5, 5]
leader = 1
a = list1[0]
for i in range(1, len(list1)):
    if leader == 0:
        a = list1[i]
    if a == list1[i]:
        leader += 1
    else:
        leader -= 1
print(a)
# 将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表。
mylist=[[1], ['a','b'], [2.3, 4.5, 6.7]]
mylist=[i for j in mylist for i in j]
print(mylist)



