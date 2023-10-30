import pygame
from datetime import datetime
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# for converting the degree / end positions of the clock hands
def degree(r, tht):
    x = math.sin(2*math.pi*(tht/360))*r
    y = math.cos(2*math.pi*(tht/360))*r
    return (x + 320, -(y-240))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    ct = datetime.now().time()
    sec = ct.second
    minu = ct.minute
    hour = ct.hour
    saat = ct.strftime("%H:%M:%S")
    pygame.display.set_caption(saat)
    window.fill((255,255,255))
    body = pygame.draw.circle(window, (0,0,0), (320, 240), 222, 4)
    cent = pygame.draw.circle(window,(0,0,0), (320,240), 10)


    # hour hand
    r_hour = 140
    tht_hour = (hour + minu/60 + sec/3600)*(360/12)
    hour_hand = pygame.draw.line(window, (0,0,0), (320, 240), degree(r_hour, tht_hour), 8)
    # minute hand
    r_min = 175
    tht_min = (minu + sec/60)*(360/60)
    minute_hand = pygame.draw.line(window, (0,0,0), (320, 240), degree(r_min, tht_min), 4)
    # second hand
    r_sec = 200
    tht_sec = sec *(360/60)
    second_hand = pygame.draw.line(window, (255,0,0), (320, 240), degree(r_sec, tht_sec), 2)

    pygame.display.flip()
    clock.tick(60)