import pygame
from .log import o
from .frame import Frame
from config import *
pygame.init()
o("游戏模块加载成功！")


class Game(Frame):
    def __init__(self):
        super().__init__()

    def command(self):
        pass
