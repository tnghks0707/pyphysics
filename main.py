import pygame
import PyphyObject
import sys
from pygame.locals import *

width = 1280
height = 720
white = (255, 255, 255)
black = (0, 0, 0)
fps = 60

pygame.init()

pygame.display.set_caption("PyPhysics")
displaysurf = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()

#pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

myimage = pygame.image.load("cur.png")
imagerect : pygame.Rect = myimage.get_rect()

po = PyphyObject.Object(myimage)
imageWidth = 0
imageHeight = 0
timedelta = 0
#imagerect.center = (width_, height_)
#imagerect.center = (0, 0)

#물리엔진
F = -9.8
m = 1.0
a = F / m
v = 0.0
distence = 0.0
timecontinue = 0.0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #물리엔진 시작
    
    timedelta_f = timedelta / 1000
    v += -a * timedelta_f
    distence += (v * timedelta_f) / 2

    distence_pixel = distence * 100

    imageHeight = distence_pixel

    if(distence_pixel > 1500):
        distence = -10.0

    #물리엔진 끝
    #imageWidth, imageHeight = pygame.mouse.get_pos()
    displaysurf.fill(black)
    imagerect.topleft = (imageWidth, imageHeight)
    displaysurf.blit(myimage, imagerect)

    pygame.display.update()
    timedelta = clock.tick(fps)
