# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

window.fill((254,245,0))
width = 640 - robot.get_width() 
height = 480 - robot.get_height()

for i in range(1000):
    x = randint(0, width)
    y = randint(0,height)
    window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


