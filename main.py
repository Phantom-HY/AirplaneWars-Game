import pygame
import home

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("飞机大战")
clock = pygame.time.Clock()

while 1:
    home.draw()
    # 退出检测 #
    flag = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flag = 0
    if flag == 0:
        break
    # 刷新屏幕 #
    pygame.display.flip()
    clock.tick(50)
