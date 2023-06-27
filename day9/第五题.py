#!/usr/bin/python
# author Yu
# 2023年06月10日
"""
a+ w+ r+
相同点：都是以可读可写的方式打开的
不同点：a+是追加的方式，当以默认为文本模式打开时，而默认光标在最后，只有结合seek才能读取
只有以二进制模式打开时，才能向前偏移
w+虽然是可读可写 ，但是一旦打开，将会将原本存在的内容清空。
r+虽然打开不会将原本内容清空，但是当写入文件时,因为文件指针在开头，所以会覆盖后面的内容
"""
import os

with open('file3.txt','w+',encoding='utf-8')as file3:
    file3.write("hello")
    file3.seek(0,os.SEEK_SET)
    a=file3.read()
    print(a)

with open("file3.txt",'a+',encoding='utf-8')as file3:
    file3.write(" python")
    file3.seek(0,os.SEEK_SET)
    a=file3.read()
    print(a)
with open("file3.txt",'r+',encoding='utf-8')as file3:
    file3.write("hh need")
    file3.seek(0,os.SEEK_SET)
    a=file3.read()
    print(a)