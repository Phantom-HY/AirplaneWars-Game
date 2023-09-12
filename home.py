import pygame

# 初始化 #
pygame.init()

# 图片 #
Map = pygame.image.load("./images/UI/map.png")
start = pygame.image.load("./images/UI/start.png")
tutorial = pygame.image.load("./images/UI/tutorial.png")
# 标题 #
title_front = pygame.font.Font("./Font/Dengl.ttf", 55)
title_en_front = pygame.font.Font("./Font/Inkfree.ttf", 60)
title = title_front.render("飞机大战", True, (255, 255, 255))
title_en = title_en_front.render("Plane Wars", True, (255, 255, 255))


screen = pygame.display.set_mode((480, 700))


def draw():
    global Map, start, tutorial
    screen.blit(Map, (0, 0))
    screen.blit(title, (120, 100))
    screen.blit(title_en, (100, 150))
    screen.blit(start, (70, 500))
    screen.blit(tutorial, (70, 550))
