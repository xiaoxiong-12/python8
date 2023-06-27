#!/usr/bin/python
# author Yu
# 2023年06月09日
class Tool(object):
    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name
        # 针对类属性做一个计数+1
        Tool.count += 1
    @classmethod
    def show_tool_count(cls):
        print(f'对象总数{cls.count}')
    @staticmethod
    def help():
        print('这个类的主要功能是使用工具')


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")
# 已经实例化的对象数目
print(Tool.count)
#类属性和类方法一般通过类来访问
print(tool3.count)
Tool.count = 0
print(Tool.count)
Tool.show_tool_count()

Tool.help()  # 静态方法一般打印帮助
