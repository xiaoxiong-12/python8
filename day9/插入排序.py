#!/usr/bin/python
# author Yu
# 2023年06月10日
class Soulution:
    def __init__(self, my_list: list):
        self.my_list = my_list
    def sort(self):
        for i in range(1,len(self.my_list)):# i就是要插入的元素的索引
            #在已序队列中遇到小的就交换
            for j in range(i):#从已序队列的头开始插
                if self.my_list[i]<self.my_list[j]:
                    self.my_list[i],self.my_list[j]=self.my_list[j],self.my_list[i]
                else:
                    break
    def sort2(self):#从已序队列的尾插
        for i in range(len(self.my_list)):
            current=self.my_list[i]#记录要插入的元素
            preindex=i-1
            while current>self.my_list[preindex] and preindex>-1:
                self.my_list[preindex+1]=self.my_list[preindex]
                preindex-=1
            self.my_list[preindex+1]=current

    def get(self):
        for i in self.my_list:
            print(i,end=' ')


if __name__ == '__main__':
    my_list = [10, 9, 1, 7, 6, 5, 4, 3, 2, 8]
    a=Soulution(my_list)
    a.sort2()
    a.get()

