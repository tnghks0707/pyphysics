import pygame
import PyphyObject
import sys
import json
from pygame.locals import *

#Build Objects from Object.json
def BuildObjects():
    jsonObject = json.load(open("Objects.json"))
    print(jsonObject["PyphyVersion"])
    pass

def main():
    BuildObjects()
    return
    
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

    #오브젝트 생성
    po = PyphyObject.Object(pygame.image.load("cur.png"))
    po.SetRigidbody(1.0)
    po.rigidbody.AddForce(PyphyObject.Vector(0, -9.8))

    timedelta = 0
    #imagerect.center = (width_, height_)
    #imagerect.center = (0, 0)

    while True:
        timedelta = clock.tick(fps)
        #print("frame : " + str(clock.get_fps()))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurf.fill(black)

        #중력가속도
        #po.rigidbody.AddForce(PyphyObject.Vector(0, -9.8))
        po.rigidbody.Calculate(timedelta)
        po.Render(displaysurf)

        pygame.display.update()    

if __name__ == "__main__":
    main()