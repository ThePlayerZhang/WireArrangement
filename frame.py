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
        self.layout = "level"
        self.mouse = (0, 0)

    def mainloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.mouse = pygame.mouse.get_pos()
        self.frame.fill(self.bg_color)
        self.frame.blit(config.frame[self.layout]["bg"], (0, 0))
        self.command()
        pygame.display.update()

    def command(self):
        pass
