#!/usr/bin/python
# author Yu
# 2023年06月07日
# 45、去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。
def work_45():
    mylist = [1, 2, 5, 2, 3, 4, 5, 'x', 4, 'x']
    mylist=list(set(mylist))
    print(mylist)
# 46、返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大下写互换形式。
def work_46():
    s = 'abCdEfg'
    # 转换为大写
    s_upper = s.upper()
    # 转换为小写
    s_lower = s.lower()
    # 大小写互换
    s_swap = s.swapcase()
    # 输出结果
    print('全部大写形式：', s_upper)
    print('全部小写形式：', s_lower)
    print('大写小写互换形式：', s_swap)
# 47、判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。
def work_47():
    mystr = 'abCdEfg'
    myupper = mystr.istitle()  # 判断首字母是否大写
    mylower = mystr.islower()  # 判断是否全为小写
    upper = mystr.isupper()  # 判断是否全为大写
    print('字符串首字母是否大写：', myupper)
    print('字符串是否全部为小写：', mylower)
    print('字符串是否全部为大写：', upper)


# 48、返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式。
def work_48():
    mystr='this is python'
    mystr=mystr.title()
    print(mystr)
# 49、判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。
def work_49():
    s = 'this is python'
    starts_with_this = s.startswith('this')  # 判断是否以'this'开头
    ends_with_python = s.endswith('python')  # 判断是否以'python'结尾
    print('字符串是否以"this"开头：', starts_with_this)
    print('字符串是否以"python"结尾：', ends_with_python)


# 50、返回字符串 ‘this is python’ 中 ‘is’ 的出现次数。
# 51、返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。
# 52、将字符串 ‘this is python’ 切片成3个单词。
# 53、返回字符串 ‘blog.csdn.net/xufive/article/details/102946961’ 按路径分隔符切片的结果。
if __name__ == '__main__':
    # work_45()
    # work_46()
    # work_47()
    work_48()
    work_49()