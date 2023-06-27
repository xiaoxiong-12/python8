#!/usr/bin/python
# author Yu
# 2023年06月11日
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class MyList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def print_list(self):
        node=self.head
        while node:
            print(node.value,end=' ')
            node=node.next
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        sorted_head:Node=self.head#将第一个元素视为已经排好序的元素
        unsorted_head:Node=self.head.next#将第二个元素视为未排好序元素的头结点
        sorted_head.next = None
        while unsorted_head:
            curr=unsorted_head#当前要插入的元素
            unsorted_head = unsorted_head.next#记录下一个要插入的元素
            if curr.value<sorted_head.value:
                curr.next=sorted_head
                sorted_head=curr
            else:
                search=sorted_head
                while search.next and search.next.value<curr.value:
                    search=search.next
                curr.next = search.next
                search.next = curr
        self.head=sorted_head

b=MyList()
a=[5,3,4,631,23,43,99]
for i in a:
    b.insert(i)
b.insertion_sort()
b.print_list()





