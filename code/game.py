import pygame
from .log import o
from .frame import Frame, quit_game
from config import *
from res.init import *

pygame.init()
o("游戏模块加载成功！")


class Game(Frame):
    def __init__(self):
        super().__init__()
        self.main_ui_y = 0  # 当进行动画时，按钮的y坐标

        self.mouse_pressed = False  # 为拖动关卡做支持
        self.mouse_last_pos = (0, 0)
        self.square_rect = img["ui.start.bg"].get_rect(center=(2048, 288))
        self.square_rect.move_ip(0, 108)

    def click_command(self, pos1, pos2):  # 判断是否按下
        if pos1[0] < self.mouse[0] < pos2[0] and pos1[1] < self.mouse[1] < pos2[1]:
            return True
        else:
            return False

    def command(self):
        self.window.blit(img[self.frame.replace(".a", "")], (0, 0))
        if self.frame == "ui.main":  # 只在主菜单下渲染
            if self.click_command((200, 280), (570, 480)):  # 开始游戏按钮
                self.window.blit(img["ui.main.button.start.click"], (0, 0))
                if pygame.mouse.get_pressed(3)[0]:
                    self.frame = "ui.start.a"
            else:
                self.window.blit(img["ui.main.button.start"], (0, 0))

            if self.click_command((640, 470), (1000, 600)):  # 设置按钮
                self.window.blit(img["ui.main.button.settings.click"], (0, 0))
                if pygame.mouse.get_pressed(3)[0]:
                    self.frame = "ui.setting.a"
            else:
                self.window.blit(img["ui.main.button.settings"], (0, 0))

            if self.click_command((110, 440), (250, 690)):  # 退出按钮
                self.window.blit(img["ui.main.button.exit.click"], (0, 0))
                if pygame.mouse.get_pressed(3)[0]:
                    quit_game()
            else:
                self.window.blit(img["ui.main.button.exit"], (0, 0))
            self.window.blit(img["ui.logo"], (0, 0))

        if self.frame in ["ui.start.a", "ui.setting.a"]:  # 当进行动画时运行
            if self.main_ui_y > 500:
                self.frame = self.frame.replace(".a", "")  # 取消动画状态
            else:
                self.main_ui_y += 15  # 动画运行代码
                self.window.blit(img["ui.main.button.start"], (0, self.main_ui_y))
                self.window.blit(img["ui.main.button.settings"], (0, self.main_ui_y * 0.9))
                self.window.blit(img["ui.main.button.exit"], (0, self.main_ui_y * 0.8))
                self.window.blit(img["ui.logo"], (0, self.main_ui_y * -1))

        if self.frame == "ui.start":
            if self.mouse_last_pos is not None and pygame.mouse.get_pressed(3)[0]:
                dx = self.mouse[0] - self.mouse_last_pos[0]
                self.square_rect.move_ip(dx, 0)
            self.mouse_last_pos = self.mouse

            # 绘制图片
            self.window.blit(img["ui.start.bg"], self.square_rect)
