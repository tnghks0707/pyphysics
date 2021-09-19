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

po = PyphyObject.Object(pygame.image.load("cur.png"))
po.SetRigidbody(1.0)

imageWidth = 0
imageHeight = 0
timedelta = 0
#imagerect.center = (width_, height_)
#imagerect.center = (0, 0)

while True:
    timedelta = clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurf.fill(black)

    po.rigidbody.AddForce(PyphyObject.Vector(-9.8, 0))
    po.rigidbody.Calculate(timedelta)
    po.Render(displaysurf)

    pygame.display.update()
