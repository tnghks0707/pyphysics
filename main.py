import pygame
import PyphyObject
import PyphyTypes
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
 
        freeze_x = False
        freeze_y = False

        rigidbody = None
        if "Rigidbody" in i:
            rigidbody = i["Rigidbody"]
            if "freeze_x" in rigidbody:
                freeze_x = rigidbody["freeze_x"]
            if "freeze_y" in rigidbody:
                freeze_y = rigidbody["freeze_y"]

        UserScript = None
        if "UserScript" in i:
            UserScript = i["UserScript"]

        image = pygame.image.load(image)
        rect : pygame.Rect = image.get_rect()
        rect.topleft = (location[0], location[1])
        newObject = PyphyObject.Object(image, rect=rect, name=name, size=(size_height, size_width), visible=visible,
        UserScript = UserScript)
        if rigidbody != None:
            newObject.SetRigidbody(rigidbody["Mess"], Fz_x = freeze_x, Fz_y = freeze_y)

        #newObject.rigidbody.AddForce(PyphyObject.Vector(0, -1000))
        #newObject.rigidbody.SetSpeed(PyphyObject.Vector(0, -1))
        
        ObjectList.append(newObject)

def main():
    BuildObjects()

    #width = 200
    height = 720
    width = 1280
    #height = 720
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

    while True:
        loopchecker += 1
        timedelta = clock.tick(fps)
        #print("frame : " + str(clock.get_fps()))

        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            pygame.event.post(event)
            """
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
        """
        

        displaysurf.fill(black)

        Object: PyphyObject.Object

        for Object_i in range(0, len(ObjectList)):
            Object = ObjectList[Object_i]

            if Object.UserScriptEnable:
                try:
                    Object.UserScript.Update(Object, pygame)
                except Exception as e:
                    print(Object.Name + " : Error executing user script \"" + Object.UserScriptPath + "\"")
                    print("--------------------------------------------")
                    print(e)
                    exit(-1)
            
            if Object.rigidbody != None:
                Object.rigidbody.AddForce(PyphyObject.Vector(0, -10))

            ObjectRect = Object.Rect
            #충돌 처리(테스트)
            #일단은 성공!
                        
            #Object.rigidbody.AddForce(PyphyObject.Vector(10, 0))
            """
            if Object.Name == "Wind":
                if left:
                    Object.rigidbody.AddForce(PyphyObject.Vector(-5, 0))
                elif right:
                    Object.rigidbody.AddForce(PyphyObject.Vector(5, 0))
                elif up:
                    Object.rigidbody.AddForce(PyphyObject.Vector(0, 25))
                elif down:
                    Object.rigidbody.AddForce(PyphyObject.Vector(0, -5))
                elif stop:
                    stop = False
                    Object.rigidbody.SetSpeed(PyphyObject.Vector(0, 0))
            """

            
            for Object2 in ObjectList[Object_i + 1:]:
                Object2Rect: pygame.Rect = Object2.Rect
                if Object != Object2 and ObjectRect.colliderect(Object2Rect):
                    #print(Object.Name + "이(가) " + Object2.Name + "와 충돌함")
                    Object2WidthLength = Object2Rect.size[0] / 2
                    Object2HeightLength = Object2Rect.size[1] / 2
                    ocw = round(Object2WidthLength * (3 / 10))
                    if ocw > 30:
                        ocw = 30
                    och = round(Object2HeightLength * (3 / 10))
                    if och > 30:
                        och = 30
                    
                    if ((Object2Rect.midtop[1] < ObjectRect.midtop[1] - 1 < Object2Rect.midbottom[1] 
                        or Object2Rect.midtop[1] < ObjectRect.midbottom[1] - 1 < Object2Rect.midbottom[1]) 
                        and Object2Rect.midright[0] - ocw < ObjectRect.midleft[0]):
                        #left
                        if(Object.rigidbody.freeze_x == False):
                            Object.rigidbody.WidthDistence = Object2Rect.midright[0]
                        
                        p1 = Object.rigidbody.GetWidthMomentum()
                        p2 = Object2.rigidbody.GetWidthMomentum()
                        Object2.rigidbody.AddWidthMomentum(p1)
                        Object.rigidbody.AddWidthMomentum(p2)

                    if ((Object2Rect.midtop[1] < ObjectRect.midtop[1] - 1 < Object2Rect.midbottom[1] 
                        or Object2Rect.midtop[1] < ObjectRect.midbottom[1] - 1 < Object2Rect.midbottom[1]) 
                        and Object2Rect.midleft[0] + ocw > ObjectRect.midright[0]):
                        #right
                        if(Object.rigidbody.freeze_x == False):
                            Object.rigidbody.WidthDistence = Object2Rect.midleft[0] - ObjectRect.size[0] + 1

                        p1 = Object.rigidbody.GetWidthMomentum()
                        p2 = Object2.rigidbody.GetWidthMomentum()
                        Object2.rigidbody.AddWidthMomentum(p1)
                        Object.rigidbody.AddWidthMomentum(p2)

                    if ((Object2Rect.midleft[0] < ObjectRect.midleft[0] < Object2Rect.midright[0]
                        or Object2Rect.midleft[0] < ObjectRect.midright[0] < Object2Rect.midright[0])
                        and Object2Rect.midbottom[1] - och < ObjectRect.midtop[1]):
                        #top
                        if(Object.rigidbody.freeze_y == False):
                            Object.rigidbody.HeightDistence = Object2Rect.midbottom[1]

                        p1 = Object.rigidbody.GetHeightMomentum()
                        p2 = Object2.rigidbody.GetHeightMomentum()
                        Object2.rigidbody.AddHeightMomentum(p1)
                        Object.rigidbody.AddHeightMomentum(p2)

                    if ((Object2Rect.midleft[0] < ObjectRect.midleft[0] < Object2Rect.midright[0]
                        or Object2Rect.midleft[0] < ObjectRect.midright[0] < Object2Rect.midright[0])
                        and Object2Rect.midtop[1] + och > ObjectRect.midbottom[1]):
                        #bottom
                        if(Object.rigidbody.freeze_y == False):
                            Object.rigidbody.HeightDistence = Object2Rect.midtop[1] - ObjectRect.size[1] + 1

                        p1 = Object.rigidbody.GetHeightMomentum()
                        p2 = Object2.rigidbody.GetHeightMomentum()
                        Object2.rigidbody.AddHeightMomentum(p1)
                        Object.rigidbody.AddHeightMomentum(p2)
                        #Object.rigidbody.HeightDistence = Object2Rect.midtop[1] -ObjectRect.size[1] + 1


                    """
                    elif Object2HeightLength - och <= ObjectRect.midtop[1] - Object2Rect.center[1] + 1 <= Object2HeightLength:
                        #top
                        p1 = Object.rigidbody.GetHeightMomentum()
                        p2 = Object2.rigidbody.GetHeightMomentum()
                        Object2.rigidbody.AddHeightMomentum(p1)
                        Object.rigidbody.AddHeightMomentum(p2)
                        print("top")
                        #Object.rigidbody.HeightDistence = Object2Rect.midtop[1] -ObjectRect.size[1] + 1

                    elif Object2HeightLength - och <= Object2Rect.center[1] - ObjectRect.midbottom[1] + 1 <= Object2HeightLength:
                        #bottom
                        p1 = Object.rigidbody.GetHeightMomentum()
                        p2 = Object2.rigidbody.GetHeightMomentum()
                        Object2.rigidbody.AddHeightMomentum(p1)
                        Object.rigidbody.AddHeightMomentum(p2)
                        print("bottom")
                    """

            
            """
            if Object.Type != PyphyTypes.Ground:
                for Grounds in ObjectList:
                    if Grounds.Type != PyphyTypes.Ground:
                        continue

                    GroundRect: pygame.Rect = Grounds.Rect
                    if Grounds != Object and ObjectRect.colliderect(GroundRect):
                        
                        GroundHeightLength = GroundRect.size[1] / 2
                        och = round(GroundHeightLength * (3 / 10))

                        if GroundHeightLength - och <= GroundRect.center[1] - ObjectRect.midbottom[1] + 1 <= GroundHeightLength:
                            #top
                            Object.rigidbody.HeightDeltaA = 0
                            Object.rigidbody.HeightA = 0
                            Object.rigidbody.HeightDistence = GroundRect.midtop[1] - ObjectRect.size[1] + 1
            """
            
            if Object.rigidbody != None:
                Object.rigidbody.Calculate(timedelta)

            Object.Render(displaysurf)

        #중력가속도
        """
        po.rigidbody.AddForce(PyphyObject.Vector(0, -9.8))
        po.rigidbody.Calculate(timedelta)
        po.Render(displaysurf)
        """

        pygame.display.flip()    

if __name__ == "__main__":
    main()
