#!/usr/bin/python
# author Yu
# 2023年06月08日
def demo1(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


# args获取的是positional参数
# kwargs 获取的是keyword参数
def demo(num, *args, **kwargs):
    print(num)
    print(args)  # 接收2, 3, 4, 5, 6（都是position参数）args打印成一个元组
    print(kwargs)  # name="小明", age=18都是keyword参数 kwargs打印成一个字典
    print('-' * 50)
    demo1(num, *args, **kwargs)
    # 进行解包如果不解包直接传参 一个元组和字典都
    # 将视为position参数传给args


demo(1, 2, 3, 4, 5, 6, name="小明", age=18)
