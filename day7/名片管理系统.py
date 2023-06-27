class Manage_Card:
    def __init__(self):
        self.card_list =[]

    def new_card(self):
        print('*' * 50)
        name = input("请输入姓名：")
        phone = input("请输入电话：")
        qq = input("请输入 QQ 号码：")
        email = input("请输入邮箱：")
        card_dict = {"name": name,
                     "phone": phone,
                     "qq": qq,
                     "email": email}
        self.card_list.append(card_dict)
        print("添加成功")

    def show_card(self):
        for i in self.card_list:
            print(i)

    def search_card(self):
        name = input("请输入姓名：")
        for i in self.card_list:
            if name in i['name']:
                print(i)
            else:
                print("没有此人")


class Main():
    def __init__(self):
        self.manage = Manage_Card()

    def print_menu(self):
        print("*" * 50)
        print("欢迎使用【菜单管理系统】")
        print("1. 新建名片")
        print("2. 显示全部")
        print("3. 查询名片")
        print("0. 退出系统")
        print("*" * 50)

    def run(self):
        while True:
            self.print_menu()
            choice = input("请输入数字选自系统")
            if choice == '1':
                self.manage.new_card()
            elif choice == '2':
                self.manage.show_card()
            elif choice == '3':
                self.manage.search_card()
            elif choice == '0':
                print("感谢使用【名片管理系统】！")
                break
            else:
                print("您的输入有误！请重新输入")


if __name__ == '__main__':
    a=Main()
    a.run()