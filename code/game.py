import pygame
from .log import o
from .frame import Frame, quit_game
from res.init import *

pygame.init()
o("游戏模块加载成功！")


class Game(Frame):
    def __init__(self):
        super().__init__()

    def click_command(self, pos1, pos2):
        if pos1[0] < self.mouse[0] < pos2[0] and pos1[1] < self.mouse[1] < pos2[1]:
            return True
        else:
            return False

    def command(self):
        self.window.blit(img[self.frame], (0, 0))
        if self.frame == "ui.main":
            if self.click_command((200, 280), (570, 480)):
                self.window.blit(img["ui.main.button.start.click"], (0, 0))
                if pygame.mouse.get_pressed(3)[0]:
                    self.frame = "ui.start"
            else:
                self.window.blit(img["ui.main.button.start"], (0, 0))

            if self.click_command((640, 470), (1000, 600)):
                self.window.blit(img["ui.main.button.settings.click"], (0, 0))
                if pygame.mouse.get_pressed(3)[0]:
                    self.frame = "ui.setting"
            else:
                self.window.blit(img["ui.main.button.settings"], (0, 0))

            if self.click_command((110, 440), (250, 690)):
                self.window.blit(img["ui.main.button.exit.click"], (0, 0))
                if pygame.mouse.get_pressed(3)[0]:
                    quit_game()
            else:
                self.window.blit(img["ui.main.button.exit"], (0, 0))
