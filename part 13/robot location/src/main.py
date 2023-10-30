import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x = randint(0, 640-robot.get_width())
y = randint(0, 480-robot.get_height())

clock = pygame.time.Clock()

while True:
    x2 = x + robot.get_width()
    y2 = y + robot.get_height()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            p = event.dict.get('pos')
            if p[0] in range(x, x2) and p[1] in range(y, y2):
                x = randint(0, 640-robot.get_width())
                y = randint(0, 480-robot.get_height())
    
    window.fill((220,190,0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
