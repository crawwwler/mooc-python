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

    if left:
        x -= 2
    if right:
        x += 2
    if up:
        y -= 2
    if down:
        y += 2

    window.fill((100,200,10))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)