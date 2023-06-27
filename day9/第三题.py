#!/usr/bin/python
# author Yu
# 2023年06月10日
with open('redme','r',encoding='utf-8') as redme:
    with open('redme1','w',encoding='utf-8') as redme1:
        data=redme.read()
        redme1.write(data)
