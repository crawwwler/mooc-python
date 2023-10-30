import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x = 0
y = 0
direction = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((202,102,0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    y += direction
    if direction > 0 and y + robot.get_height() >= 480:
        direction = -direction
    if direction < 0 and y <= 0:
        direction = -direction
    clock.tick(60)