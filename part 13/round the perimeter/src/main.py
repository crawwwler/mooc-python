import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x = 0
y = 0
hor = 1
ver = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0,0,88))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += hor
    y += ver

    if hor > 0 and x + robot.get_width() >= 640 :
        hor = 0
        ver = 1
    if ver > 0 and y + robot.get_height() >= 480 :
        hor = -1
        ver = 0
    if hor < 0 and x <= 0 :
        hor = 0 
        ver = -1
    if ver < 0 and y <= 0 :
        hor = 1 
        ver = 0
    clock.tick(60)

    
