#!/usr/bin/python
# author Yu
# 2023年06月12日
class Sort:
    def __init__(self,my_list):
        self.my_list=my_list
        self.length=len(self.my_list)
    def bubble_sort(self):
        for i in range(self.length):
            for j in range(self.length-i-1):
                if self.my_list[j]>self.my_list[j+1]:
                    self.my_list[j],self.my_list[j+1]=self.my_list[j+1],self.my_list[j]
    def select_sort(self):
        # 基于冒泡的改进，当发现后面一个较小元素时，不立马交换，只记录其索引，遍历完一次后在交换
        for i in range(self.length):
            curr=i
            for j in range(i+1,self.length):
                if self.my_list[j]<self.my_list[curr]:
                    curr=j
            self.my_list[i],self.my_list[curr]=self.my_list[curr],self.my_list[i]
    def insert_sort(self):
        for i in range(self.length):
            curr=self.my_list[i]#记录当前要插入的元素
            pre_index=i-1
            while curr < self.my_list[pre_index] and pre_index>-1:#找寻要插入的位置
                self.my_list[pre_index + 1] = self.my_list[pre_index]
                pre_index -= 1
            self.my_list[pre_index+1]=curr#插入元素



a=[1,32342,432,23,43,234,24,2321,99]
sort=Sort(a)
# sort.bubble_sort()
# sort.select_sort()
sort.insert_sort()
print(sort.my_list)
