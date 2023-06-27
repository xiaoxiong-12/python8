#!/usr/bin/python
# author Yu
# 2023年06月12日
# 2、完成二叉树的层次建树，前序遍历，中序遍历，后序遍历，层序遍历
class Node:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []
        self.queue2=[]#重新定义了一个列表，如果用queue的话，会导致insert_node无法用

    def insert_node(self, value):#层次建树
        node = Node(value)
        self.queue.append(node)
        if self.root is None:
            self.root = node
        elif self.queue[0].lchild is None:
            self.queue[0].lchild = node
        elif self.queue[0].rchild is None:
            self.queue[0].rchild = node
            self.queue.pop(0)

    def pre_order(self,node:Node):#前序遍历
        print(node.value,end=' ')
        if node.lchild:
            self.pre_order(node.lchild)
        if node.rchild:
            self.pre_order(node.rchild)
    def mid_order(self,node):#中序遍历
        if node:
            self.mid_order(node.lchild)
            print(node.value,end=' ')
            self.mid_order(node.rchild)
    def post_order(self,node):#后序遍历
        if node:
            self.post_order(node.lchild)
            self.post_order(node.rchild)
            print(node.value,end=' ')
    def level_order(self):#层次遍历
        if self.root is None:
            print("树为空")
            return
        self.queue2.append(self.root)
        while self.queue2:
            if self.queue2[0].lchild is not None:
                self.queue2.append(self.queue2[0].lchild)
                if self.queue2[0].rchild is not None:
                    self.queue2.append(self.queue2[0].rchild)
            print(self.queue2[0].value,end='  ')
            self.queue2.pop(0)



a=Tree()
for i in range(11):
    a.insert_node(i)
a.pre_order(a.root)
print()
a.mid_order(a.root)
print()
a.post_order(a.root)
print()
a.level_order()