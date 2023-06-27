#!/usr/bin/python
# author Yu
# 2023年06月12日
class Quicksort:
    def __init__(self, my_list: []):
        self.my_list = my_list

    def sort(self):
        if len(self.my_list) < 2:
            return
        left = 0
        right = len(self.my_list) - 1
        self.quicksort(left, right)

    def quicksort(self, left, right):
        if left >= right:
            return
        low = left
        high = right
        flag = 0
        pivot = self.my_list[left]
        while left < right:
            if flag == 0:
                if self.my_list[right] > pivot:
                    right -= 1
                else:
                    self.my_list[left] = self.my_list[right]
                    left += 1
                    flag = 1
            else:
                if self.my_list[left] < pivot:
                    left += 1
                else:
                    self.my_list[right] = self.my_list[left]
                    right -= 1
                    flag = 0
        self.my_list[left] = pivot
        self.quicksort(low, left - 1)
        self.quicksort(right + 1, high)


a = Quicksort([10, 12, 5, 4, 123, 3234, 3, 32, 25, 52])
a.sort()
print(a.my_list)
