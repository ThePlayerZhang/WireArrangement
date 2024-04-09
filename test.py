import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口的大小
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 加载图片
square_image = pygame.image.load('./res/bg/main.png')
square_rect = square_image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# 跟踪鼠标是否按下
mouse_pressed = False
mouse_last_pos = None

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
            mouse_last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_pressed:
                mouse_pos = event.pos
                if mouse_last_pos is not None:
                    dx = mouse_pos[0] - mouse_last_pos[0]
                    dy = mouse_pos[1] - mouse_last_pos[1]
                    square_rect.move_ip(dx, dy)
                mouse_last_pos = mouse_pos

                # 填充背景颜色
    screen.fill((0, 0, 0))

    # 绘制图片
    screen.blit(square_image, square_rect)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    CLOCK = pygame.time.Clock()
    CLOCK.tick(60)