import sys
import os
name='day'+sys.argv[1]+'_熊佳宇.tar.gz '  #拼名字
#os.system是Python调用bash shell的函数
os.system('tar czf '+name+"*.py")  #压缩
str_scp='scp '+name+' python8@42.192.117.114:~/day'+sys.argv[1]
os.system(str_scp)
print('提交成功')