import pygame
from random import randint
pygame.init()
class Robot:
    def __init__(self):
        self._rob = pygame.image.load("robot.png")
        self._x = randint(0, 640-self._rob.get_width())
        self._y = 0 - self._rob.get_height()
        self._height = self._rob.get_height()
    
    def build(self):
        window.blit(self._rob, (self.x, self.y))
    def move(self):
        if self._y + self.height < 480:
            self._y += 1
    def hide_to_left(self):
        self._x -= 1
    def hide_to_right(self):
        self._x += 1
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def height(self):
        return self._height

window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
robots = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 
    if randint(1, 99) == 1:
        robots.append(Robot())
    window.fill((100,100,100))
    for robot in robots:
        robot.move()
        robot.build()
        if robot.y + robot.height >= 480:
            if robot.x < 320:
                robot.hide_to_left()
            else:
                robot.hide_to_right()
    robot = [robot for robot in robots if robot.y + robot.height < 480]
    pygame.display.flip()
    clock.tick(60)