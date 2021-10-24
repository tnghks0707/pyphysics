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
            newObject.SetRigidbody(rigidbody["Mess"])

        #newObject.rigidbody.AddForce(PyphyObject.Vector(0, -1000))
        #newObject.rigidbody.SetSpeed(PyphyObject.Vector(0, -1))
        
        ObjectList.append(newObject)

def main():
    BuildObjects()

    #width = 800
    #height = 450
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

    loopchecker = 0

    left = False
    right = False
    up = False
    down = False
    stop = False

    lastp = 0
    lastdddd = False

    while True:
        loopchecker += 1
        timedelta = clock.tick(fps)
        #print("frame : " + str(clock.get_fps()))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                elif event.key == pygame.K_RIGHT:
                    right = True
                elif event.key == pygame.K_UP:
                    up = True
                elif event.key == pygame.K_DOWN:
                    down = True
                elif event.key == pygame.K_SPACE:
                    stop = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                elif event.key == pygame.K_RIGHT:
                    right = False
                elif event.key == pygame.K_UP:
                    up = False
                elif event.key == pygame.K_DOWN:
                    down = False

        displaysurf.fill(black)

        Object: PyphyObject.Object

        for Object in ObjectList:
            if Object.rigidbody != None:
                Object.rigidbody.Calculate(timedelta)
            ObjectRect = Object.Rect
            #충돌 처리(테스트)
            
                        
            #Object.rigidbody.AddForce(PyphyObject.Vector(10, 0))
            if Object.Name == "Wind":
                if left:
                    Object.rigidbody.AddForce(PyphyObject.Vector(-5, 0))
                elif right:
                    Object.rigidbody.AddForce(PyphyObject.Vector(5, 0))
                elif up:
                    Object.rigidbody.AddForce(PyphyObject.Vector(0, 5))
                elif down:
                    Object.rigidbody.AddForce(PyphyObject.Vector(0, -5))
                elif stop:
                    stop = False
                    Object.rigidbody.SetSpeed(PyphyObject.Vector(0, 0))

                

                for Object2 in ObjectList:
                    Object2Rect: pygame.Rect = Object2.Rect
                    if Object != Object2 and ObjectRect.colliderect(Object2Rect):
                        Object2WidthLength = Object2Rect.size[0] / 2
                        Object2HeightLength = Object2Rect.size[1] / 2
                        if Object2WidthLength - 8 <= ObjectRect.midleft[0] - Object2Rect.center[0] + 1 <= Object2WidthLength:
                            #left
                            p1 = Object.rigidbody.GetWidthMomentum()
                            p2 = Object2.rigidbody.GetWidthMomentum()
                            if p1 <= 0:
                                Object2.rigidbody.AddWidthMomentum(p1)
                            Object.rigidbody.AddWidthMomentum(p2)

                        if Object2WidthLength - 8 <= Object2Rect.center[0] - ObjectRect.midright[0] + 1 <= Object2WidthLength:
                            #right
                            p1 = Object.rigidbody.GetWidthMomentum()
                            p2 = Object2.rigidbody.GetWidthMomentum()
                            if p1 >= 0:
                                Object2.rigidbody.AddWidthMomentum(p1)
                            Object.rigidbody.AddWidthMomentum(p2)

                        if Object2HeightLength - 8 <= ObjectRect.midtop[1] - Object2Rect.center[1] + 1 <= Object2HeightLength:
                            #top
                            p1 = Object.rigidbody.GetHeightMomentum()
                            p2 = Object2.rigidbody.GetHeightMomentum()
                            if p1 >= 0:
                                Object2.rigidbody.AddHeightMomentum(p1)
                            Object.rigidbody.AddHeightMomentum(p2)

                        if Object2HeightLength - 8 <= Object2Rect.center[1] - ObjectRect.midbottom[1] + 1 <= Object2HeightLength:
                            #bottom
                            p1 = Object.rigidbody.GetHeightMomentum()
                            p2 = Object2.rigidbody.GetHeightMomentum()
                            if p1 <= 0:
                                Object2.rigidbody.AddHeightMomentum(p1)
                            Object.rigidbody.AddHeightMomentum(p2)


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
