#!/usr/bin/python
# author Yu
# 2023年06月12日
# 1、实现有5个元素的循环队列（本身列表大小是6个）
class CircleQueue:
    def __init__(self):
        self.queue = [0] * 6
        self.front = 0
        self.rear = 0
        self.size=6

    def enqueue(self,value):#进队要先判断队列是否满
        if (self.rear+1)%self.size==self.front:
            print("队列已满")
            return False
        else:
            self.queue[self.rear]=value
            self.rear=(self.rear+1)%self.size
    def dequeue(self):#判断队列是否为空
        if self.rear==self.front:
            print("队列为空")
        else:
            print(self.queue[self.front])
            self.front=(self.front+1)%self.size#进行取模运算，否则当front等于5时会出错
circlequeue=CircleQueue()
for i in range(6):
    circlequeue.enqueue(i)
print(circlequeue.queue)
circlequeue.dequeue()
circlequeue.enqueue(20)
print(circlequeue.queue)
