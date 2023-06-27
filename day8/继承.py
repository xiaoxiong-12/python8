#!/usr/bin/python
# author Yu
# 2023年06月09日
class Animal:
    def eat(self):
        print("快乐的吃")
    @staticmethod
    def drink():
        print("欢快的喝")
    def sleep(self):
        print("安静的睡")
class Dog(Animal):
    def run(self):
        print("飞快的跑")
    def drink(self):
        super().drink()#拿到父类的方法
        print("调皮的喝")
        # 重写了父类 查找方法是优先查找自
        # 己类里面，然后再往父亲的类里找，最后找object


class XiaoTianDog(Dog):
    def fly(self):
        print("飞")

if __name__ == '__main__':
    # Animal.drink()
    a=Dog()
    a.drink()
    a.run()
    a.sleep()
    b=XiaoTianDog()
    b.fly()
