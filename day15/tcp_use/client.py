#!/usr/bin/python
# author Yu
# 2023年06月17日
# tcp客户端
import socket
import threading


def tcp_client():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect(('192.168.1.16', 9999))
    receive_thread = threading.Thread(target=receive, args=(tcp_client,))
    receive_thread.start()
    while True:
        data = input('')
        data_bytes = data.encode('utf-8')
        tcp_client.send(data_bytes)
    tcp_client.close()  # 关闭客户端套接字


def receive(tcp_client):
    while True:
        data_bytes = tcp_client.recv(64)
        data = data_bytes.decode('utf-8')
        print('', data)


tcp_client()
