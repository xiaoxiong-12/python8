#!/usr/bin/python
# author Yu
# 2023年06月15日
"""
sorted会返回一个新的列表
sort是对原有列表进行排序
"""


def use_sort():
    my_list = [3, 1, 4, 2, 5]
    my_list_sort = sorted(my_list)
    print(my_list_sort)
    print(my_list)  # 原有列表没有被改变
    my_list.sort()
    print(my_list)


print(sorted("This is a test string from Andrew".split(), key=str.lower))
print(sorted("This is a test string Andrew".split(), key=lambda x: 'A' if 'i' in x else 'H'))
print('*' * 100)

import operator

student_tuples = [
    ('john', 'B', 15),
    ('jane', 'B', 12),
    ('dave', 'A', 16),
]
print(sorted(student_tuples, key=lambda x:x[2]))
# itemgetter 函数来获取可迭代对象中的元素
#itemgetter(2)就是获取可迭代对象中索引为2的元素
print(sorted(student_tuples,key=operator.itemgetter(2)))
print('*'*100)
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        """
        str必须返回一个字符串,而repr返回一个对象的字符串表示形式，可以返回非字符串类型
        :return:
        """
        return repr((self.name, self.grade, self.age))
def sort_own_object():
    student_objects = [
        Student('john', 'B', 15),
        Student('jane', 'B', 12),
        Student('dave', 'A', 16),
    ]
    a=sorted(student_objects,key=operator.attrgetter('age','name'))
#attrgetter是获取对象中属性来作为排序依据
    print(a)
sort_own_object()