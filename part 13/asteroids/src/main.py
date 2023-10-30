import pygame
from random import randint

pygame.init()
class Rock:
    def __init__(self):
        self._rock = pygame.image.load("rock.png")
        self._x = randint(0,640-self._rock.get_width())
        self._y = 0-self._rock.get_height()
        self._out = False
    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    
    def height(self):
        return self._rock.get_height()
    def width(self):
        return self._rock.get_width()
    def move(self):
            self._y += 1
    def build(self):
        window.blit(self._rock, (self.x, self.y))
    def disapear(self):
        self._out = True
    def isout(self):
        return self._out
    def bottom(self):
        return self.y + self._rock.get_height()
    

class Scoreboard:
    def __init__(self):
        self._point = 0
        self._sb = self.result()
    
    def result(self):
        font = pygame.font.SysFont("Arial", 16, True, False)
        txt = font.render(f"Points: {self._point}", True, (255,0,0))
        window.blit(txt, (550, 4))
    
    def scored(self):
        self._point += 1

    def missed(self):
        font = pygame.font.SysFont("Arial", 32, True)
        txt = font.render("GAME OVER!", True, (255,0,0))
        window.blit(txt, (320-txt.get_width()/2, 240-txt.get_height()/2))

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("asteroids")
robot = pygame.image.load("robot.png")
sb = Scoreboard()
clock = pygame.time.Clock()

xot = 10
yot = 480 - robot.get_height()

left = False
right = False

rocks = []

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
    
    if left :
        xot -= 2
    if right:
        xot += 2
    
    window.fill((0,0,0))
    window.blit(robot, (xot, yot))
    sb.result()

    if randint(1, 166) == 1 :
        rocks.append(Rock())

    for rock in rocks:
        rock.move()
        rock.build()
        if rock.bottom() in range(yot, yot + robot.get_height()) and rock.x in range(xot, xot + robot.get_width()):
            sb.scored()
            rock.disapear()
        elif rock.y >= 480 :
            sb.missed()
            break
    rocks = [rock for rock in rocks if not rock.isout()]
    pygame.display.flip()
    clock.tick(60)