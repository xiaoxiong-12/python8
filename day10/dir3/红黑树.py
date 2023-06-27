#!/usr/bin/python
# author Yu
# 2023年06月11日
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = None  # 可能的取值为 "RED" 或 "BLACK"

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # 创建新节点并进行初始化
        node = Node(key)
        node.color = "RED"

        # 插入新节点
        if self.root is None:
            self.root = node
        else:
            self._insert_node(self.root, node)

        # 修正红黑树的性质
        self._fix_violations(node)

    def _insert_node(self, root, node):
        # 递归地插入新节点到红黑树
        if node.key < root.key:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                self._insert_node(root.left, node)
        else:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self._insert_node(root.right, node)

    def _fix_violations(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                # Case 1: 叔叔节点为红色
                if uncle is not None and uncle.color == "RED":
                    # 当前节点的父节点和叔叔节点都变为黑色
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    # 当前节点的祖父节点变为红色
                    node.parent.parent.color = "RED"
                    # 将当前节点移动到祖父节点，继续修正
                    node = node.parent.parent
                else:
                    # Case 2: 叔叔节点为黑色，当前节点为右孩子
                    if node == node.parent.right:
                        # 将当前节点移动到父节点，左旋转
                        node = node.parent
                        self._rotate_left(node)

                    # Case 3: 叔叔节点为黑色，当前节点为左孩子
                    # 将当前节点的父节点变为黑色，祖父节点变为红色，右旋转
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                # Case 1: 叔叔节点为红色
                if uncle is not None and uncle.color == "RED":
                    # 当前节点的父节点和叔叔节点都变为黑色
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    # 当前节点的祖父节点变为红色
                    node.parent.parent.color = "RED"
                    # 将当前节点移动到祖父节点，继续修正
                    node = node.parent.parent
                else:
                    # Case 2: 叔叔节点为黑色，当前节点为左孩子
                    if node == node.parent.left:
                        # 将当前节点移动到父节点，右旋转
                        node = node.parent
                        self._rotate_right(node)

                    # Case 3: 叔叔节点为黑色，当前节点为右孩子
                    # 将当前节点的父节点变为黑色，祖父节点变为红色，左旋转
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._rotate_left(node.parent.parent)

        self.root.color = "BLACK"

    def _rotate_left(self, node):
        # 左旋转操作
        temp = node.right
        node.right = temp.left
        if temp.left is not None:
            temp.left.parent = node
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def _rotate_right(self, node):
        # 右旋转操作
        temp = node.left
        node.left = temp.right
        if temp.right is not None:
            temp.right.parent = node
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp

# 创建一个红黑树对象
rb_tree = RedBlackTree()

# 插入一些数据进行验证
data = [10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 8, 11, 14, 17, 25]

for key in data:
    rb_tree.insert(key)

# 打印红黑树中的节点
def print_rb_tree(node, indent=""):
    if node is None:
        return

    color = "BLACK" if node.color == "BLACK" else "RED"
    print(indent + str(node.key) + " (" + color + ")")

    print_rb_tree(node.left, indent + "  ")
    print_rb_tree(node.right, indent + "  ")

# 打印红黑树
print_rb_tree(rb_tree.root)




