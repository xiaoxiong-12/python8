#!/usr/bin/python
# author Yu
# 2023年06月09日
# 将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。
my_str='2.72, 5, 7, 3.14'
a=my_str.split(',')#去除','并放入列表
print(list(map(lambda x:float(x) if '.'in x else int(x),a)))
print(list(map(lambda x:int(x) if '.'not in x else float(x),a)))
print(list(map(lambda x:int(x)*5 if '.'not in x else float(x)-1,a)))
#{map(函数,迭代器)}也是一个迭代器
#lambda 匿名函数：x是传入的参数
#:后写对参数x的处理