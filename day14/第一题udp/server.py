#!/usr/bin/python
# author Yu
# 2023年06月16日
from socket import socket as sk
import socket
def udp_server():
    udp_sk = sk(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sk.bind(('',9999))  # ''等价与0.0.0.0
    while True:
        recv_data,recv_addr=udp_sk.recvfrom(1000)
        if recv_data.decode('utf-8')=='1':
            print("退出连接")
            break
        print('接收内容：',recv_data.decode('utf-8'))
        data=input("请输入文字：")
        data=data.encode('utf-8')
        udp_sk.sendto(data,recv_addr)
    udp_sk.close()
udp_server()