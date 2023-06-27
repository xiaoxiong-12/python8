#!/usr/bin/python
# author Yu
# 2023年06月17日
import socket
import threading

class TcpClient:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        self.tcp_client=None
    def start(self):
        self.tcp_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_client.connect((self.ip,self.port))
        receive_thread=threading.Thread(target=self.revceive)
        receive_thread.start()
        self.send()

    def revceive(self):
        data_bytes=self.tcp_client.recv(64)
        data=data_bytes.decode('utf-8')
        if data == 'exit':
            self.__close()
            return
        elif data[0]=='1':
            string=data.split('+')
            with open(string[0][1:],'w',encoding='utf-8')as file:
                file.write(string[1])
        else:
            print('收到的消息：',data)
    def send(self):
        while True:
            data=input("请输入发送内容：")
            data_bytes=data.encode('utf-8')
            self.tcp_client.send(data_bytes)
            if data=='exit':
                break
        self.__close()
    def __close(self):
        self.tcp_client.close()
if __name__ == '__main__':
    tcp_client=TcpClient('192.168.1.16',9999)
    tcp_client.start()