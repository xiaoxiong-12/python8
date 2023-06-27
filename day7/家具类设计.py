#!/usr/bin/python
# author Yu
# 2023年06月08日
# 先设计家具，再设计房子，因为被依赖的类要先设计
class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.name}！面积：{self.area}'
    # 重写后打印对象既可以返回这个


# 1. 创建家具
bed = HouseItem("席梦思", 4)
print(bed)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []
        # 初始化

    def __str__(self):
        # Python 能够自动的将一对括号内部的代码连接在一起
        return ((f'{self.house_type},面积 {self.area},'
                 f'剩余面积{self.free_area},{self.item_list} '))

    #:HouseItem是注解技术，为了编程联想
    def add_item(self, item: HouseItem):
        if self.free_area < item.area:
            print('房子没空间了，不能放了')
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


# 2. 创建房子对象
my_home = House("两室一厅", 60)
print(my_home)
print('-' * 50)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
