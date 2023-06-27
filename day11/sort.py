#!/usr/bin/python
# author Yu
# 2023年06月13日
import random

class Sort:
    def __init__(self,num_range):
        self.my_list = [0] * 10
        self.length = len(self.my_list)
        self.num_range=num_range

    def random_data(self):
        for i in range(self.length):
            self.my_list[i] = random.randint(0,self.num_range)

    def quciksort(self, left, right):
        if left < right:
            x = self.quick(left, right)
            self.quciksort(left, x - 1)
            self.quciksort(x + 1, right)

    def quick(self, left, right):
        k = left
        for i in range(left, right):
            if self.my_list[i] < self.my_list[right]:
                if k != i:
                    self.my_list[i], self.my_list[k] = self.my_list[k], self.my_list[i]
                k += 1
        self.my_list[right], self.my_list[k] = self.my_list[k], self.my_list[right]
        return k

    def adjust_max_heap(self, adjust_pos, length):
        mylist = self.my_list
        dad = adjust_pos
        son = dad * 2 + 1  # 左孩子
        while son < length:
            if son + 1 < length and mylist[son] < mylist[son + 1]:
                son = son + 1
            if mylist[son] > mylist[dad]:
                mylist[son], mylist[dad] = mylist[dad], mylist[son]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def head_sort(self):
        adjust_pos = self.length >> 2 - 1
        for i in range(adjust_pos, -1, -1):
            self.adjust_max_heap(i, self.length)  # 调整为大根堆
        for i in range(self.length - 1, -1, -1):
            self.my_list[0], self.my_list[i] = self.my_list[i], self.my_list[0]
            self.adjust_max_heap(0, i)

    def merge(self, left, right, mid):
        i = left
        j = mid + 1
        k = left
        my_list_backup = self.my_list.copy()
        while i <= mid and j <= right:
            if my_list_backup[i] < my_list_backup[j]:
                self.my_list[k] = my_list_backup[i]
                i += 1
            else:
                self.my_list[k] = my_list_backup[j]
                j += 1
            k += 1
        while i <= mid:
            self.my_list[k] = my_list_backup[i]
            i += 1
            k += 1
        while j <= mid:
            self.my_list[k] = my_list_backup[j]
            j += 1
            k += 1

    def merge_sort(self, left, right):
        if left < right:
            mid = (right + left) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, right, mid)
    def cout_sort(self):
        cout=[0]*self.num_range
        for i in self.my_list:
            cout[i]+=1
        k=0
        for i in range(self.num_range):
            while cout[i]!=0:
                self.my_list[k]=i
                cout[i]-=1
                k+=1



a = Sort(99)
a.random_data()
print(a.my_list)
# a.quciksort(0,a.length-1)
a.head_sort()
# a.merge_sort(0, a.length - 1)
# a.cout_sort()
print(a.my_list)
