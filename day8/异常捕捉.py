#!/usr/bin/python
# author Yu
# 2023年06月09日
# 通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，
# 12321就是对称数，
# 123321也是对称数，否则就不是
try:
    data = input("请输入整数:")
    num = int(data)
except ValueError:
    print("值错误！！请输入整数:")
except Exception as a:
    print("异常错误")
else:
    start = 0
    end = -1
    for i in range(len(data) // 2):
        if data[start] == data[end]:
            start += 1
            end -= 1
        else:
            print("不是对称数")
            break
    if start == len(data) // 2:
        print("是对称数")
