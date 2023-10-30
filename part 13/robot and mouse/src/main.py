import pygame 
pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
x = 320 - robot.get_width()/2
y = 240 - robot.get_height()/2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        try:
            x = event.dict.get('pos')[0] - robot.get_width()/2
            y = event.dict.get('pos')[1] - robot.get_height()/2
        except:
            x = x
            y = y
    window.fill((69,138,69))
    window.blit(robot, (x,y))
    pygame.display.flip()
    clock.tick(60)