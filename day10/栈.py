#!/usr/bin/python
# author Yu
# 2023年06月10日
class Stack:
    def __init__(self):
        self.stack=[]
    def pop(self):
        return self.stack.pop()
    def push(self,data):
        self.stack.append(data)
    def print_list(self):
        print(self.stack)

a=Stack()
a.push(1)
a.push(2)
print(a.pop())
a.print_list()