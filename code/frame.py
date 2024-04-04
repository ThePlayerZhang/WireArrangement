# qwq 已完成编辑（可能吧） qwq

import sys
import pygame
from .log import o, save_log
from config import *
pygame.init()
o("窗体模块加载成功！")


def quit_game():
    o("正在退出...")
    pygame.quit()
    save_log()
    sys.exit()


class Frame(object):
    def __init__(self):
        o("开始加载窗体...")
        self.frame = frame  # 当前页面
        self.fps = fps  # 刷新率
        self.mouse = [0, 0]  # 当前鼠标位置
        self.key = []  # 被按下的按键
        self.window = pygame.display.set_mode(size)
        o("加载窗体完成！")

    def command(self):
        pass  # 由子类自定义

    def mainloop(self):
        for event in pygame.event.get():  # 经典检查退出
            if event.type == pygame.QUIT:
                quit_game()
        self.mouse = pygame.mouse.get_pos()
        self.key = pygame.key.get_pressed()
        self.command()
        pygame.display.update()
