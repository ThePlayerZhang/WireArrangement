import pygame
from .log import o
from .frame import Frame
from res.init import *
pygame.init()
o("游戏模块加载成功！")


class Game(Frame):
    def __init__(self):
        super().__init__()

    def command(self):
        self.window.blit(img[self.frame], (0, 0))
        if self.frame == "ui.main":
            self.window.blit(img["ui.main.button.start"], (0, 0))
            self.window.blit(img["ui.main.button.settings"], (0, 0))
            self.window.blit(img["ui.main.button.exit"], (0, 0))
