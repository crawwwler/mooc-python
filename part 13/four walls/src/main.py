import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x = 0
y = 0
clock = pygame.time.Clock()
right = False
left = False
up = False
down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
        if event.type == pygame.QUIT:
            exit()
    if x <= 0:
        left = False
    if y <= 0:
        up = False
    if x + robot.get_width() >= 640 :
        right = False
    if y + robot.get_height() >= 480:
        down = False
        
    if left:
        x -= 2
    if right:
        x += 2
    if up:
        y -= 2
    if down:
        y += 2

    window.fill((44,215,188))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)