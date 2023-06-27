#!/usr/bin/python
# author Yu
# 2023年06月08日
# 37、创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
def create_set():
    my_set = set()
    for i in ['x', 'y', 'z']:
        my_set.add(i)
    print(my_set)


# 38、删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增j加元素 ‘w’，然后清空整个集合。
def del_set():
    my_set = {'x', 'z', 'y'}
    my_set.remove('z')
    my_set.add('w')
    print(my_set)


# 39、返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。
def difference():
    my_set = {'A', 'D', 'B'}
    my_set2 = {"D", 'E', 'C'}
    print(my_set - my_set2)


# 40、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集。
def union():
    my_set = {'A', 'D', 'B'}
    my_set2 = {"D", 'E', 'C'}
    print(my_set | my_set2)


# 41、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集。
def intersection():
    my_set = {'A', 'D', 'B'}
    my_set2 = {"D", 'E', 'C'}
    print(my_set & my_set2)


# 42、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。
def set_():
    my_set = {'A', 'D', 'B'}
    my_set2 = {"D", 'E', 'C'}
    print(my_set ^ my_set2)


# 43、判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。
def bool_set():
    my_set = {'A', 'D', 'B'}
    my_set2 = {"D", 'E', 'C'}
    if len(my_set | my_set2) < (len(my_set) + len(my_set2)):
        print("有重复元素")
    else:
        print("没有重复元素")


# 44、判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。
def bool_set2():
    my_set = {'A', 'C'}
    my_set2 = {"D", 'C', 'A', 'E'}
    print(my_set.issubset(my_set2))


if __name__ == '__main__':
    create_set()
    del_set()
    difference()
    union()
    intersection()
    set_()
    bool_set()
    bool_set2()
