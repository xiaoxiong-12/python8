#!/usr/bin/python
# author Yu
# 2023年06月16日
import socket
import sys
def udp_client():
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        print("输入1断开连接")
        data = input("请输入文字：")
        udp_client.sendto(data.encode('utf-8'), (sys.argv[1], 9999))
        if data=='1':
            print("退出连接")
            break
        recv_data, _ = udp_client.recvfrom(1000)#会卡住
        data = recv_data.decode('utf-8')
        print('接收内容：', data)
    udp_client.close()
udp_client()