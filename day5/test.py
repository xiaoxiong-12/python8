#!/usr/bin/python
# author Yu
# 2023年06月06日

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = ListNode(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def out(self):
        while True:
            if self.head.next != None:
                print(self.head.val)
                self.head = self.head.next
            else:
                print(self.head.val)
                break

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        pass


if __name__ == '__main__':
    a = Solution()
    a.insert(3)
    a.insert(4)
    a.insert(2)
    b=Solution()
    b.insert(4)
    b.insert(6)
    b.insert(5)

