#!/usr/bin/python
# author Yu
# 2023年06月11日
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        self.parent=None
        self.color=None
class RedBlackTree:
    def __init__(self):
        self.root:Node=None
    def insert(self,value):
        node=Node(value)
        if self.root is None:
            self.root=node
            self.root.color='BLACK'
        else:
            self.insert_node(self.root,node)
    def insert_node(self,root,node):
        if root.value<node.value:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self.insert_node(root.right,node)
        else:
            if root.left is None:
                root.left=node
                node.parent=root
            else:
                self.insert_node(root.left,node)




    def out(self,node=None):
        if node is None:
            node=self.root
        if node.left is not None:
            self.out(node.left)
        print(node.value)
        if node.right is not None:
            self.out(node.right)



a=RedBlackTree()
data = [10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 8, 11, 14, 17, 25]
for i in data:
    a.insert(i)
print(a.root.color)