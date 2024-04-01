import pygame

timestamp = "%Y-%m-%d %H:%M:%S"
frame_size = (1280, 720)
frame_bg_color = (40, 70, 130)
output = "[%s][%s] %s"
highlight = [
    [60, 80, 4, 8],
    [60, 80, 4, 8]
]

frame = {
    "level": {
        "bg": pygame.image.load("./res/pic/bg.jpg")
    }
}
