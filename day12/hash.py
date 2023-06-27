MAXKEY = 1000
from collections import deque
def elf_hash(hash_str: str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        h &= ~g
    return h % MAXKEY

def use_hash(hash_list: list):
    stu_list = [('xiongda', 98.2), ('lele', 97.1), ('hanmeimei', 88), ('wangdao', 69), ('fenghua', 72)]
    for i in stu_list:
        hash_value = elf_hash(i[0])
        if hash_list[hash_value] is None:
            hash_list[hash_value] = i
        else:
            if isinstance(hash_list[hash_value],tuple):
                mydeque=deque()
                mydeque.append(hash_list[hash_value])
                mydeque.append(i)
                hash_list[hash_value]=mydeque
            else:
                hash_list[hash_value].append(i)
def hash_search(hash_list,str_name):
    hash_value=elf_hash(str_name)
    if hash_list[hash_value] is not None:
        print(hash_list[hash_value])
    else:
        print("没有此字符串")


hash_list = [None] * MAXKEY
use_hash(hash_list)
hash_search(hash_list,'xiongda')