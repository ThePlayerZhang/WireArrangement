from . import frame
import pygame


class Game(frame.Frame):
    def __init__(self):
        super().__init__()

    def command(self):
        if self.layout == "level":
            pass