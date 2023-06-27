#!/usr/bin/python
# author Yu
# 2023年06月09日
class Printer:
    instance=None
    flag=False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance

    def __init__(self,data):
        if self.flag==False:
            self.data=data
            self.flag=True

    def start(self):
        print(self.data)

a=Printer("hello")
b=Printer("hi")
print(id(a))
print(id(b))
a.start()
b.start()
print(a.data)
