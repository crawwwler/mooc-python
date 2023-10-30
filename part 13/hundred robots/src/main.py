# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")


width = robot.get_width()
height = robot.get_height()
window.fill((10,88,44))
y = 88
helper = 66
for i in range(10):
    x = helper
    for j in range(10):
        window.blit(robot, (x,y))
        x += width - width// 4
    y += (height//4)
    helper += (width//4)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
