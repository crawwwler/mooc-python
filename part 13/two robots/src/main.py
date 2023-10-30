import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x1 = 0
x2 = 0
y1 = 66
y2 = 200
dir1 = 1
dir2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()
    
    window.fill((14,24,34))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    
    x1 += dir1
    x2 += dir2
    if dir1 > 0 and x1 + robot.get_width() >= 640 :
        dir1 = -dir1
    if dir2 > 0 and x2 + robot.get_width() >= 640 :
        dir2 = -dir2
    if dir1 < 0 and x1 <= 0 :
        dir1 = -dir1
    if dir2 < 0 and x2 <= 0 :
        dir2 = -dir2
    clock.tick(60)
    
