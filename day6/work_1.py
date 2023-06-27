#!/usr/bin/python
# author Yu
# 2023年06月07日
# 第一题
# 列表
def use_list():
    mylist = [x for x in range(10)]
    mylist.append(999)
    mylist.extend([2, 2, 3])
    mylist.insert(3, 9)
    mylist.sort()
    a = mylist.count(2)
    print(a)
    mylist.remove(7)
    print(mylist)
    a = mylist.pop(5)
    print(a)
    print('*' * 10)
    del mylist[5]
    print(mylist)
    print('*' * 20)
    a = mylist.index(999)
    mylist.reverse()
    mylist.clear()
    print(mylist)


# 元组
def use_tuple():
    mytuple = (2,)
    # print(mytuple)
    print(mytuple.index(2))
    mytuple=(2,4,56,65,4)
    print(mytuple[2:])


# 字典
def use_dict():
    tinydict = {'a': 1, 'b': 2, 'c': '3'}
    tinydict['aa']=9
    print(tinydict)
    a=tinydict.pop('c')
    print(a)
    del tinydict['aa']
    print(tinydict)
    tinydicttwo={'la':10,'fads':1324}
    tinydict.update(tinydicttwo)
    print("a"in tinydict)


# 字符串
def use_str():
    my_string = "Helloworld"
    print(len(my_string))
    print(my_string[2:])#切片
    print(my_string.isalnum())
    my_list = ["apple", "banana", "cherry"]
    my_string = ",".join(my_list)
    print(my_string)
    my_list = my_string.split(", ")
    print(my_list)
    my_string = "apple\nbanana\ncherry"
    my_list = my_string.splitlines()
    my_string = "Hello, world"
    index = my_string.find("world")
    my_string = "Hello, world"
    new_string = my_string.replace("world", "Python")
    print(new_string)


if __name__ == '__main__':
    # use_list()
    use_tuple()
    # use_dict()
    # use_str()

"""
列表和字典都是可变数据类型，元组是不可变数据类型，一旦创建就不允许修改
字典是用哈希实现，是用空间换时间的，能以o（1）的时间复杂度找到对应的值
列表和元组都支持切边操作
字典中是无序的，以键值对存储
"""
