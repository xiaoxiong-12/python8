#!/usr/bin/python
# author Yu
# 2023年06月17日
import socket
import threading
class TcpServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.tcp_sock = None
        self.client_sock = None
        self.client_addr = None

    def start(self):
        # 1.创建套接字
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #
        self.tcp_sock.bind((self.ip, self.port))  # 参数是一个元组，由ip地址和端口号组成
        self.tcp_sock.listen(10)  # 设置最大监听客户数量
        # 接收客户端的请求,三次握手，建立连接，返回一个元组，
        # 元组第一个元素是客户端的套接字，第二个元素是客户端的地址
        self.client_sock, self.client_addr = self.tcp_sock.accept()
        # 创建一个线程，用于接收客户端发送的消息，因为接收消息是阻塞的，所以需要一个线程
        receive_thread = threading.Thread(target=self.receive, args=(self.client_sock,))
        receive_thread.start()
        self.send()

    def receive(self, client_sock):
        while True:
            data_bytes = client_sock.recv(64)#接收64个字节
            data = data_bytes.decode('utf-8')#解码
            if data=='exit':
                self.__close()
                return
            else:
                print()
                print('收到消息：', data)

    def send(self):
        while True:
            data=input("请输入发送内容：")
            data_bytes = data.encode('utf-8')
            if data[0]=='1':
                with open(data[1:],'rb')as file:
                    content=file.read()
                    data_bytes=data_bytes+'+'.encode('utf8')+content
            self.client_sock.send(data_bytes)
            if data=='exit':
                break
        self.__close()

    def __close(self):
        self.client_sock.close()  # 关闭客户端套接字
        self.tcp_sock.close()  # 关闭服务端套接字
if __name__ == '__main__':
    tcp_server=TcpServer('',9999)
    tcp_server.start()
