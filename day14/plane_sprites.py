#!/usr/bin/python
# author Yu
# 2023年06月16日
import random

import pygame
pygame.init()
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
HERO_FIRE_EVENT = pygame.USEREVENT + 1

#自定义事件，定义了一个计时器，每一秒钟触发一次
CREATE_ENEMY_EVENT = pygame.USEREVENT
pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1, x_speed=0):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)  # 传图片的位置，用相对路径
        self.rect = self.image.get_rect()  # 获取图像的尺寸
        self.speed = speed  # 垂直移动速度
        self.x_speed = x_speed  # 横向移动速度

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed  # 图像垂直移动
        self.rect.x += self.x_speed  # 图像横向移动


class BackGround(GameSprite):  # 背景对象
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height  # 实现背景图片流动


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1, 3)

        # 3. 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width  # 减去自身宽度
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()#杀掉敌机 防止内存泄露


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -5)

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()


class Bomb(GameSprite):
    def __init__(self):
        super().__init__('./images/bomb.png', -10)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 是图像初始位置为下方正中间
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 子弹精灵组
        self.bullets = pygame.sprite.Group()
        self.bomb = pygame.sprite.Group()

    def update(self):
        self.rect.y += self.speed  # 图像垂直移动
        self.rect.x += self.x_speed  # 图像横向移动
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):
        for i in (0, 1, 2):
            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            # 子弹要从飞机中间去发射
            bullet.rect.centerx = self.rect.centerx
            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet)

    def bombing(self):
        bomb = Bomb()
        bomb.rect.bottom = self.rect.y - 2 * 20
        bomb.rect.centerx = self.rect.centerx
        self.bomb.add(bomb)
