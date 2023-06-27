#!/usr/bin/python
# author Yu
# 2023年06月09日
class Product:
    def __init__(self,name,cost_price):
        self.name=name
        self.cost_price=cost_price
    def show(self):
        print(self.name)
        print(self.cost_price)

class Price:
    def __init__(self,__product:Product):
        self.__product=__product
    def __discount(self):
        self.__product.cost_price=self.__product.cost_price*2
    def show(self):
        self.__discount()
        print(f"商品名：{self.__product.name} 价格：{self.__product.cost_price}")

if __name__ == '__main__':
    product=Product('大米',1.5)
    print(product.name)
    a=Price(product)
    a.show()
"""
私有属性和方法只允许在类里面访问
"""
