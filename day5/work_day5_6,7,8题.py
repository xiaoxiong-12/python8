#!/usr/bin/python
# author Yu
# 2023年06月06日
# 使用列表的增删改查
def use_list():
    mylist = []
    mylist.append(10)
    mylist.insert(0, 9)
    mylist.extend(['猴哥', '王小二'])
    print(mylist)
    print("*" * 10)
    mylist.pop(2)
    del mylist[0]
    print(mylist)
    mylist.remove(10)
    print(mylist)
    print("*" * 10)
    mylist[0] = 6
    print(mylist)


# 7、求两个有序数字列表的公共元素
def pub():
    list_one = [7, 13, 21, 24]
    list_two = [4, 7, 9, 13, 26]
    print(set(list_one) & set(list_two))


# 8给定一个n个整型元素的列表a，其中有一个元素出现次数超过n / 2，求这个元素
def count_a():
    list1 = [2, 2, 2, 2, 2, 2, 2, 22, 432, 43, 1, 34]
    mylist=list(set(list1))
    for i in mylist:
        if list1.count(i)>len(list1)/2:
            print(i)



if __name__ == '__main__':
    use_list()
    pub()
    count_a()
