# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
width = robot.get_width()
#height = robot.get_height()
sp = [48,88]
window.fill((144,0,0))
for i in range(10):
    window.blit(robot, sp)
    sp[0] += width

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

