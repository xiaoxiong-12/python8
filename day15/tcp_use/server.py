#!/usr/bin/python
# author Yu
# 2023年06月17日
# tcp服务端
import socket
import threading


def tcp_server():
    # 1.创建套接字
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #
    tcp_sock.bind(("", 9999))  # 参数是一个元组，由ip地址和端口号组成
    tcp_sock.listen(10)  # 设置最大监听客户数量
    # 接收客户端的请求,三次握手，建立连接，返回一个元组，
    # 元组第一个元素是客户端的套接字，第二个元素是客户端的地址
    client_sock, client_addr = tcp_sock.accept()
    # 创建一个线程，用于接收客户端发送的消息，因为接收消息是阻塞的，所以需要一个线程
    receive_thread = threading.Thread(target=receive, args=(client_sock,))
    receive_thread.start()
    while True:
        data = input("")
        data_bytes = data.encode('utf-8')
        client_sock.send(data_bytes)
    client_sock.close()  # 关闭客户端套接字
    tcp_sock.close()  # 关闭服务端套接字


def receive(client_sock):
    while True:
        data_bytes = client_sock.recv(64)
        data = data_bytes.decode('utf-8')
        print(data)


tcp_server()
