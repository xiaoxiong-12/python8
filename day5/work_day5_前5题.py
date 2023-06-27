#!/usr/bin/python
# author Yu
# 2023年06月06日
import say_hi


# 1.简单的for循环，从1打印到20，横着打为1排
def use_for():
    for i in range(1, 21):
        print(i, end='  ')


"""
打印hello
"""


# 2.say_hello函数打印多次hello并给该函数加备注
def say_hello(num):
    for i in range(num):
        print("hello")


# 代码理解，不可变类型进行赋值后，内存地址将会改变
# 4.可变类型用接口改变数据后，内存地址不变 +=是相当于extend 也不会改变内存地址
def understand_type(myint, mystr, mylist, mydict):
    # int
    myint = 10
    print('函数中内存地址int：', id(myint))
    print('-' * 10)
    # str
    mystr = 'hello'
    print('函数中内存地址str：', id(mystr))
    print('-' * 10)
    # list
    mylist.append(10)
    print('函数中内存地址list：', id(mylist))
    print('-' * 10)
    # dict
    mydict['19'] = 10
    print('函数中内存地址dict：', id(mydict))
    print('-' * 10)


# 5.局部变量和全局变量
# 局部变量作用范围一般是在函数内，全局变量全局都能使用
# 使用全局变量时得声明global
LL = 9


def use_global():
    a = 10  # 在函数内使用局部变量
    global LL
    LL = 11
    print(LL)


if __name__ == '__main__':
    use_for()
    print('-' * 10)
    say_hello(5)
    print('-' * 10)
    #4题
    say_hi.say_hi1()
    say_hi.say_hi2()
    say_hi.say_hi3()
    myint = 100
    print('函数中内存地址int：',id(myint))
    mystr = 'sdf'
    print('函数中内存地址str：',id(mystr))
    mylist = [1, 124]
    print('函数中内存地址list：',id(mylist))
    mydict = {}
    print('函数中内存地址dict：',id(mydict))
    print('-' * 10)
    understand_type(myint, mystr, mylist, mydict)
    use_global()
