import pygame
from model import timestamp as t, game

pygame.init()

t.output("Hello from WireArrangement, the first output!", t.i)

main_frame = game.Game()
while True:
    main_frame.mainloop()
