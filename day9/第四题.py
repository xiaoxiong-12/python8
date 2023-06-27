#!/usr/bin/python
# author Yu
# 2023年06月10日
import os

with open('file2.txt','r',encoding='utf-8')as file:
    file.seek(5,os.SEEK_SET)
    data=file.read()
    print(data)