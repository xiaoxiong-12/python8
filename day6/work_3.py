#!/usr/bin/python
# author Yu
# 2023年06月07日
# 20、将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。
def work_20():
    mylist = ['x', 'y', 'z']
    mylist2 = [1, 2, 3]
    result_list = [(mylist[i], mylist2[i]) for i in range(3)]
    print(result_list)
    # gpt的方法
    # list1 = ['x', 'y', 'z']
    # list2 = [1, 2, 3]
    # result_list = list(zip(list1, list2))
    # print(result_list)


# 21、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键。
def work_21():
    mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    mylist = []
    for i in mydict:
        mylist.append(i)
    print(mylist)


# 22、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值。
def work_22():
    mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    mylist = []
    for j in mydict.values():
        mylist.append(j)
    print(mylist)


# 23、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组。
def work_23():
    mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    for i in mydict.items():
        print(i)


# 24、向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17。
def work_24():
    mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    mydict['David'] = 19
    print(mydict)


# 25、删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典。
def work_25():
    mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    mydict.pop('Beth')
    print(mydict)
    mydict.clear()
    print(mydict)


# 26、判断 David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中。
def bool_(data):
    mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    if data in mydict:
        print('在')
    else:
        print("不在")


def work_26():
    data1 = "David"
    data2 = "Alice"
    bool_(data1)
    bool_(data2)


# 27、遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对。
def work_27():
    mydict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    for i in mydict:
        print(i)
        print(mydict[i])


# 29、以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典。
def work_29():
    mylist = ['A', 'B', 'C', "D", 'E', 'F', 'G', 'H']
    mydict = {}
    for i in mylist:
        mydict[i] = 0
    print(mydict)


# 30、将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
def work_30():
    mylist = [['a', 1], ['b', 2]]
    mytuple = (('x', 3), ('y', 4))
    mydict1 = {}
    mydict2 = {}
    for i in mylist:
        mydict1[i[0]] = i[1]
    print(mydict1)
    for i in mytuple:
        mydict2[i[0]] = i[1]
    print(mydict2)


# 31、将元组 (1,2) 和 (3,4) 合并成一个元组。
def work_31():
    mytuple1 = (1, 2)
    mytuple2 = (3, 4)
    a = list(mytuple1) + list(mytuple2)
    print(tuple(a))


# 32、将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z。
def work_32():
    mytuple = (1, 2, 3)
    x, y, z = mytuple
    print(x, y, z)


# 33、返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号。
def work_33():
    mytuple = ('Alice', 'Beth', 'Cecil')
    print(mytuple.index('Cecil'))


# 34、返回元组 (2,5,3,2,4) 中元素 2 的个数。
def work_34():
    mytuple=(2,5,3,2,4)
    print(mytuple.count(2))
# 35、判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中。
def work_35():
    mytuple=('Alice', 'Beth', 'Cecil')
    if 'Cecil' in mytuple:
        print("yes")
    else:
        print("no")
# 36、返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组。
def work_36():
    mytuple=(2,5,3,7)
    mylist=list(mytuple)
    mylist.insert(2,9)
    mytuple=tuple(mylist)
    print(mytuple)
# 37、创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
def work_37():
    myset=set()
    myset.update({'x','y','z'})
    print(myset)

if __name__ == '__main__':
    # work_20()
    # work_21()
    # work_22()
    # work_23()
    # work_24()
    # work_25()
    # work_26()
    # work_27()
    # work_29()
    # work_30()
    # work_31()
    # work_32()
    # work_33()
    # work_34()
    # work_35()
    work_36()
    work_37()
