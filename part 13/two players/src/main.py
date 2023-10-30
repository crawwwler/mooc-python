import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x1 = 0
y1 = 0
x2 = 640 - robot.get_width()
y2 = 480 - robot.get_height()

up1 = False
down1 = False
left1 = False
right1 = False
up2 = False
down2 = False
left2 = False
right2 = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up1 = True
            if event.key == pygame.K_DOWN:
                down1 = True
            if event.key == pygame.K_LEFT:
                left1 = True
            if event.key == pygame.K_RIGHT:
                right1 = True
            if event.key == pygame.K_w:
                up2 = True
            if event.key == pygame.K_s:
                down2 = True
            if event.key == pygame.K_a:
                left2 = True
            if event.key == pygame.K_d:
                right2 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up1 = False
            if event.key == pygame.K_DOWN:
                down1 = False
            if event.key == pygame.K_LEFT:
                left1 = False
            if event.key == pygame.K_RIGHT:
                right1 = False
            if event.key == pygame.K_w:
                up2 = False
            if event.key == pygame.K_s:
                down2 = False
            if event.key == pygame.K_a:
                left2 = False
            if event.key == pygame.K_d:
                right2 = False
        if event.type == pygame.QUIT:
            exit()
    
    if up1:
        y1 -= 2
    if up2:
        y2 -= 2
    if down1:
        y1 += 2
    if down2:
        y2 += 2
    if left1:
        x1 -= 2
    if left2:
        x2 -= 2
    if right1:
        x1 += 2
    if right2:
        x2 += 2
    window.fill((4,4,4))
    window. blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    clock.tick(60)