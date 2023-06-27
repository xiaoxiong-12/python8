#!/usr/bin/python
# author Yu
# 2023年06月12日
import os

# print(os.listdir())
print(os.listdir())


def use_os(dir, width):
    for i in os.listdir(dir):
        print(" " * width, i)
        b = os.path.join(dir, i)
        a = os.path.isdir(b)
        if a:
            use_os(b, width + 4)


use_os('.', 0)
