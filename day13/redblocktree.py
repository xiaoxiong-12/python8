#!/usr/bin/python
# author Yu
# 2023年06月15日
RED = 0
BLACK = 1


class Node:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None
        self.parent = None
        self.color = 0


class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            cur = self.root
            while cur:
                pre = cur
                if cur.value < node.value:
                    cur = cur.rchild
                else:
                    cur = cur.lchild
            if pre.value < node.value:
                pre.rchild = node
                node.parent = pre
            else:
                pre.lchild = node
                node.parent = pre
        self.fix_node(node)
        self.root.color = BLACK

    def fix_node(self, node):
        if node.parent.color == BLACK:
            pass
        else:#情形三
            if node.parent.parent.rchild and node.parent.parent.rchild == RED:
                node.parent.color = RED
                node.parent.parent = BLACK
                node.parent.parent.rchild = RED
            else:
                if node.value > node.parent.value:
                    self.left_rotation(node)  # 情形四
                    node, node.parent = node.parent, node
                self.right_rotation(node)# 情形五

    def right_rotation(self, node):
        pass

    def left_rotation(self, node):
        grandparent = node.parent.parent
        grandparent.lchild = node


tree = RBTree()
my_list = [10, 32, 43, 24, 455, 521]
for i in my_list:
    tree.insert(i)
