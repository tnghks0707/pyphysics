import pygame
import PyphyObject
import sys
import json
from pygame.locals import *

ObjectList = []

#Build Objects from Object.json
def BuildObjects():
    jsonObject = json.load(open("Objects.json"))
    version = jsonObject["PyphyVersion"]
    global ObjectList
    for i in jsonObject["Objects"]:
        name = i["Name"]
        location = i["Location"]
        size = i["Size"]
        size_height = size[0]
        size_width = size[1]
        image = i["Image"]
        visible = i["Visible"]

        rigidbody = None
        if "Rigidbody" in i:
            rigidbody = i["Rigidbody"]

        image = pygame.image.load(image)
        rect : pygame.Rect = image.get_rect()
        rect.topleft = (location[0], location[1])
        newObject = PyphyObject.Object(image, rect=rect, name=name, size=(size_height, size_width), visible=visible)
        if rigidbody != None:
            newObject.SetRigidbody(rigidbody["Mass"])

        newObject.rigidbody.AddForce(PyphyObject.Vector(0, -50))
        
        ObjectList.append(newObject)

def main():
    BuildObjects()

    width = 1280
    height = 720
    white = (255, 255, 255)
    black = (0, 0, 0)
    fps = 60

    pygame.init()

    pygame.display.set_caption("PyPhysics")
    displaysurf = pygame.display.set_mode((width, height), 0, 32)
    clock = pygame.time.Clock()

    """
    pic = pygame.image.load("cur.png")
    pic2 = pygame.transform.scale(pic, (320, 240))
    pic = pygame.transform.smoothscale(pic, (320, 240))
    """

    #pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

    #오브젝트 생성

    """
    po = PyphyObject.Object(pygame.image.load("cur.png"))
    po.SetRigidbody(1.0)
    po.rigidbody.AddForce(PyphyObject.Vector(0, -9.8))
    """

    timedelta = 0
    #imagerect.center = (width_, height_)
    #imagerect.center = (0, 0)

    pygame.event.clear()

    global ObjectList

    while True:
        timedelta = clock.tick(fps)
        #print("frame : " + str(clock.get_fps()))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurf.fill(black)

        for Object in ObjectList:
            #Object.rigidbody.AddForce(PyphyObject.Vector(0, -9.8))
            Object.rigidbody.Calculate(timedelta)
            Object.Render(displaysurf)

        #중력가속도
        """
        po.rigidbody.AddForce(PyphyObject.Vector(0, -9.8))
        po.rigidbody.Calculate(timedelta)
        po.Render(displaysurf)
        """

        pygame.display.update()    

if __name__ == "__main__":
    main()