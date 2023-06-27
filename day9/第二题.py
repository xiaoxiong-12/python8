#!/usr/bin/python
# author Yu
# 2023年06月10日
with open('file2.txt','r',encoding='utf-8') as file:
    while True:
        data = file.readline()
        # 判断是否读到内容
        if not data:
            break
        print(data, end="")

