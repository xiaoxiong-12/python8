#!/usr/bin/python
# author Yu
# 2023年06月12日
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def add_node(self, value):#增加节点
        node = Node(value)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def print_data(self):#打印节点
        if self.head is None:
            print("链表为空")
            return
        else:
            node=self.head
            while node:
                print(node.value, end=' ')
                node=node.next

    def del_data(self,value):
        node=self.head
        pre:Node=None
        while node:
            if node.value==value:
                if pre is None:
                    self.head=node.next
                elif node.next is None:
                    pre.next=None
                else:
                    pre.next=node.next
                print("删除成功")
                break
            else:
                pre=node
                node=node.next

a=LinkList()
for i in range(5):
    a.add_node(i)
a.del_data(4)
a.print_data()




