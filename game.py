import frame
import pygame


class Game(frame.Frame):
    def __init__(self):
        super().__init__()

    def command(self):
        if self.layout == "level":
            if 64 < self.mouse[0] < 668 and 64 < self.mouse[1] < 668:
                pos = (int((self.mouse[0]-60)/76)*76+64, int((self.mouse[1]-60)/76)*76+64)
                self.frame.blit(pygame.image.load("./res/pic/mouse.png"), pos)