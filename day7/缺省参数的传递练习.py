#!/usr/bin/python
# author Yu
# 2023年06月08日
def add_numbers(x, y=2):
    sum_ = x + y
    return sum_


print(add_numbers(5))
print(add_numbers(3, 4))


def print_info(name, title="", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
        print(name,title,gender_text)
    else:
        print(name,title,gender_text)


print_info("小明")
print_info("老王", title="班长")
print_info("小美", gender=False)

if __name__ == '__main__':
    pass
