import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
ball = pygame.image.load("ball.png")

x = 0
y = 0
hor = 1
ver = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((200,10,170))
    window.blit(ball, (x,y))
    pygame.display.flip()

    x += hor 
    y += ver
    if hor > 0 and x + ball.get_width() >= 640:
        hor = -hor
    if hor < 0 and x <= 0:
        hor = -hor
    if ver > 0 and y + ball.get_height() >= 480:
        ver = -ver
    if ver < 0 and y <= 0 :
        ver = -ver
    clock.tick(120)