import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

robots = 10
step = 2 * math.pi / robots
angles = [i * step for i in range(robots)]
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 100, 200))
    for i in range(len(angles)):
        x = 320 + math.cos(angles[i]) * 125 - robot.get_width() / 2
        y = 240 + math.sin(angles[i]) * 125 - robot.get_height() / 2
        window.blit(robot, (x, y))
        angles[i] += 0.01
    pygame.display.flip()
    clock.tick(60)
