#!/usr/bin/python
# author Yu
# 2023年06月14日
import random


class Sort:
    def __init__(self, num_range, length):
        self.my_list = [0] * length
        self.num_range = num_range
        self.length = length
        self.random_data()

    def random_data(self):
        for i in range(self.length):
            self.my_list[i] = random.randint(0, self.num_range)

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

    def binary_search(self,num):
        low=0
        high=self.length-1
        while low<=high:
            mid=(low+high)>>1
            if num ==self.my_list[mid]:
                print(mid)
                print(num)
                print("查找成功")
                return True
            elif num<self.my_list[mid]:
                high=mid-1
            else:
                low=mid+1



sort = Sort(100, 8)
print(sort.my_list)
sort.quciksort(0,sort.length-1)
print(sort.my_list)
sort.binary_search(sort.my_list[0])