#!/usr/bin/python
# author Yu
# 2023年06月07日
# 3、将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表。
def combine():
    mytuple = (1, 2, 3)
    myset = {4, 5, 6}
    mylist1 = list(mytuple)
    mylist1.extend(list(myset))
    print(mylist1)


# 4、在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0。
def add():
    mylist = [1, 2, 3, 4, 5, 6]
    mylist.insert(0, 7)
    mylist.append(0)
    print(mylist)


# 5、反转列表 [0,1,2,3,4,5,6,7] 。
def use_reverse():
    mylist = [0, 1, 2, 3, 4, 5, 6, 7]
    mylist.reverse()
    print(mylist)


# 6、反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号。
def use_re():
    mylist = [0, 1, 2, 3, 4, 5, 6, 7]
    mylist.reverse()
    a = mylist.index(5)
    print(a)


# 7、分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
def count():
    mylist = [True, False, 0, 1, 2]
    print("True出现的次数{}".format(mylist.count(True)))
    print("False", mylist.count(False))
    print("0", mylist.count(0))
    print("1", mylist.count(1))
    print("2", mylist.count(2))  # 在python中0和FALSE  1和TRUE是等价的


# 8、从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。
def dell():
    mylist = [True, 1, 0, 'x', None, 'x', False, 2, True]
    i = 0
    while True:
        if mylist[i] == 'x':
            del mylist[i]
            i = i - 1
        i = i + 1
        if i > len(mylist) - 1:
            break
    print(mylist)
    # gpt回答的方法
    # mylist = [True, 1, 0, 'x', None, 'x', False, 2, True]
    # # 遍历列表中的每一个元素
    # for i in mylist[:]:
    #     if i == 'x':  # 判断是否为目标元素
    #         mylist.remove(i)  # 调用列表的 remove() 方法删除元素
    # print(mylist)  # 输出删除'x'后的列表


# 9、从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素。
def del_index():
    mylist = [True, 1, 0, 'x', None, 'x', False, 2, True]
    mylist.pop(4)
    print(mylist)


# 10、删除列表中索引号为奇数（或偶数）的元素。
def del_o():
    mylist = [3, 8, 5, 7]
    for i in mylist[:]:
        if i % 2 == 0:
            mylist.remove(i)
    print(mylist)


# 11、清空列表中的所有元素。
def clear_list():
    mylist = [3, 8, 5, 7]
    mylist.clear()
    print(mylist)


# 12、对列表 [3,0,8,5,7] 分别做升序和降序排列。
def sort():
    mylist = [3, 0, 8, 5, 7]
    mylist.sort()
    print(mylist)
    mylist.sort(reverse=True)
    print(mylist)


# 13、将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0。
def work_13():
    mylist = [3, 0, 8, 5, 7]
    for i in range(len(mylist)):
        if mylist[i] > 5:
            mylist[i] = 1
        else:
            mylist[i] = 0
    print(mylist)


# 14、遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号。
def work_14():
    mylist = ["x", "y", "z"]
    for i in range(len(mylist)):
        print("元素值：{}".format(mylist[i]))
        print("索引号：{}".format(i))


# 15、将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表。
def work_15():
    mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    mylist1 = []
    mylist2 = []
    for i in mylist[:]:
        if i % 2 == 0:
            mylist1.append(i)
        else:
            mylist2.append(i)
    print(mylist1)
    print(mylist2)


# 16、分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序。
def work_16():
    mylist = [[6, 5], [3, 7], [2, 8]]
    mylist.sort()
    print(mylist)


# 17、从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素。
def work_17():
    mylist = [1, 4, 7, 2, 5, 8]
    mylist2=['x','y','z']
    for i in range(len(mylist2)):
        mylist.insert(i+3,mylist2[i])
    print(mylist)

# 18、快速生成由 [5,50) 区间内的整数组成的列表。
def work_18():
    mylist=[i for i in range(5,50)]
    print(mylist)
if __name__ == '__main__':
    # combine()
    # add()
    # use_reverse()
    # use_re()
    # count()
    # dell()
    # del_index()
    # del_o()
    # clear_list()
    # sort()
    # work_13()
    # work_14()
    # work_15()
    # work_16()
    # work_17()
    work_18()
