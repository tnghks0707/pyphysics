import pygame

class Object:
    Name: str
    Surface: pygame.Surface
    Rect: pygame.Rect
    rigidbody = None
    Visible = True

    def __init__(self, Isurface, rect=None, name=None, size=None, visible=True):
        self.Surface = Isurface
        self.Visible = visible
        if rect != None:
            self.Rect = rect
        else:
            self.Rect = self.Surface.get_rect()
        if name != None:
            self.Name = name
        if size != None:
            self.Surface = pygame.transform.smoothscale(self.Surface, size)
    
    def SetRigidbody(self, mass):
        self.rigidbody = Rigidbody(self.Rect, mass)

    def TransformScale(self, size):
        self.Surface = pygame.transform.smoothscale(self.Surface, size)

    def Render(self, displaysurf):
        if self.Visible == True:
            displaysurf.blit(self.Surface, self.Rect)



class Rigidbody:
    Rect = None
    Mass = 0.0
    HeightF = 0.0
    HeightA = 0.0
    HeightDeltaA = 0.0

    HeightDistence = 0.0

    HeightF_lasttime = 0
    
    WidthDistence = 0.0

    def __init__(self, Rect: pygame.Rect, mass):
        self.Rect = Rect
        self.Mess = mass
        (self.WidthDistence, self.HeightDistence) = Rect.topleft
        pass

    def AddForce(self, vector):
        self.HeightF += vector.getHeightF()

    def Calculate(self, timeDelta):
        self.HeightA = self.HeightF / self.Mess
        self.HeightF = 0

        timedelta_f = timeDelta / 1000
        #지속시간에 더함
        #timecontinue += timedelta_f

        self.HeightDeltaA += self.HeightA * timedelta_f
        self.HeightDistence -= self.HeightDeltaA * timedelta_f * 100

        self.Rect.topleft = (self.WidthDistence, self.HeightDistence)

        print(self.HeightDeltaA)

        if(self.HeightDistence > 1500):
            self.HeightDistence = -10.0



class Vector:
    HeightF = 0.0
    WidthF = 0.0
    
    def __init__(self, WidthF, HeightF):
        self.HeightF = HeightF
        self.WidthF = WidthF

    def getHeightF(self):
        return self.HeightF
