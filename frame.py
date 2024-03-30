import pygame
import sys
import config
import timestamp as t
pygame.init()


class Frame:
    def __init__(self):
        t.output("Initialize display...", t.i)
        self.frame = pygame.display.set_mode(config.frame_size)
        self.bg_color = config.frame_bg_color
        t.output("finnish initialize display...", t.i)

    def mainloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.frame.fill(self.bg_color)
        pygame.display.update()
