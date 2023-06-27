#!/usr/bin/python
# author Yu
# 2023年06月05日
# 通过print输出变量的类型
def view_var():
    apple_price = 10
    str_ = 'jade'
    print(type(apple_price))
    print(type(str_))


# 使用input读取变量
def use_input():
    name = input("请输入你的名字:")
    num = input("请输入你的年龄:")
    print("{}今年{}岁!".format(name, num))
    num = input("请输入要乘以2的数字:")
    print(int(num) * 2)


# 统计一个整数对应的二进制数的1的个数
def count_bin():
    num = input("请输入一个整数:")
    num_int = int(num)
    bits = bin(num_int & ((1 << 64) - 1))
    print(bits)
    sum_ = 0
    for i in bits:
        if i == '1':
            sum_ = sum_ + 1
    print(sum_)


# 有3个数出现了两次一个数出现了一次，找出出现了一次的那个数
# 异或就有交换律 与0异或等于其本身 与相同的数异或得0  同0异一
def once():
    list_int = [8, 2, 3, 9, 3, 2, 8]
    result = 0
    for num in list_int:
        result = result ^ num
    print(result)


# 有3个数出现了两次二个数出现了一次，找出出现了一次的那两个数
def two():
    list_int = [8, 2, 3, 9, 4, 3, 2, 8]
    result = 0
    for num in list_int:
        result = result ^ num
    result = result & (-1) * result
    num1 = 0
    num2 = 0
    for i in range(len(list_int)):
        if (result & list_int[i]):
            num1 = num1 ^ list_int[i]
        else:
            num2 = num2 ^ list_int[i]
    print(num1)
    print(num2)


# 两数求和
def twosum():
    nums = [3, 2, 4]
    target = 6
    a = {}  # 字典
    for i, num in enumerate(nums):
        if target - num in a:
            print(a[target - num], i)
        a[num] = i  # 把列表的索引当成字典的值（value），把列表的值当成字典的键（key）


if __name__ == '__main__':
    # twosum()
    # view_var()
    # use_input()
    # count_bin()
    two()
    # once()
