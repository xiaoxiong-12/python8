#!/usr/bin/python
# author Yu
# 2023年06月16日

# 屏幕大小的常量对象
from plane_sprites import *




class PlaneGame:
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏的窗口大小为（480,700）
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建刷新频率
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建,也是初始化
        self.__create_sprites()
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)
    def __create_sprites(self):
        #绘制背景精灵
        a = BackGround()
        b = BackGround(True)
        self.back_group = pygame.sprite.Group(a, b)  # 两张背景图，所以是两个精灵
        #绘制我方战机
        self.hero=Hero()
        self.hero_group=pygame.sprite.Group(self.hero)

        self.enemy_group=pygame.sprite.Group()


    def __update_sprites(self):
        self.back_group.draw(self.screen)  # 绘图 背景图
        self.back_group.update()  # 更新整个组的对象(两张背景图)

        self.hero_group.draw(self.screen)  # 绘图 我方战机
        self.hero_group.update()  # 更新整个组的对象(两张背景图)

        self.hero.bullets.draw(self.screen)#子弹
        self.hero.bullets.update()

        self.enemy_group.draw(self.screen)
        self.enemy_group.update()

        self.hero.bomb.draw(self.screen)
        self.hero.bomb.update()
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # elif event.type == HERO_FIRE_EVENT:#自定义事件，每30秒调用一下开火函数
            #     self.hero.fire()

            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)


        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.x_speed = 8
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.x_speed = -8
        elif keys_pressed[pygame.K_UP]:
            self.hero.speed = -8
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed = 8
        elif keys_pressed[pygame.K_SPACE]:
            self.hero.fire()
        elif keys_pressed[pygame.K_q]:
            self.hero.bombing()
        else:
            self.hero.speed = 0
            self.hero.x_speed=0
    def start_game(self):
        while True:
            self.clock.tick(30)  # 设置刷新率
            self.__event_handler()
            self.__update_sprites()#更新精灵的绘制
            pygame.display.update()

    @staticmethod#静态方法
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()  # 进程结束


if __name__ == '__main__':
    pygame.init()
    b = PlaneGame()
    b.start_game()
