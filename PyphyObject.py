import pygame
import ctypes

class Object:
    Surface: pygame.Surface
    Rect: pygame.Rect
    rigidbody = None

    def __init__(self, Isurface, rect=None):
        self.Surface = Isurface
        self.Rect = self.Surface.get_rect()
        if rect != None:
            self.Rect = rect
    
    def SetRigidbody(self, mass):
        self.rigidbody = Rigidbody(self.Rect, mass)

    def Render(self, displaysurf):
        displaysurf.blit(self.Surface, self.Rect)



class Rigidbody:
    Rect = None
    Mass = 0.0
    HeightF = 0.0
    HeightA = 0.0
    HeightDeltaA = 0.0
    HeightDistence = 0.0
    HeightF_lasttime = 0

    def __init__(self, Rect, mass):
        self.Rect = Rect
        self.Mess = mass
        pass

    def AddForce(self, vector):
        self.HeightF += vector.getHeightF()

    def Calculate(self, timeDelta):
        self.HeightA = self.HeightF / self.Mess
        self.HeightF = 0
        
        (imageWidth, imageHeight) = self.Rect.topleft

        timedelta_f = timeDelta / 1000
        #지속시간에 더함
        #timecontinue += timedelta_f

        self.HeightDeltaA += self.HeightA * timedelta_f
        self.HeightDistence -= self.HeightDeltaA * timedelta_f
    
        distence_pixel = self.HeightDistence * 100

        self.Rect.topleft = (imageWidth, distence_pixel)

        print(self.HeightDeltaA)

        if(distence_pixel > 1500):
            self.HeightDistence = -10.0



class Vector:
    HeightF = 0.0
    WidthF = 0.0
    
    def __init__(self, HeightF, WidthF):
        self.HeightF = HeightF
        self.WidthF = WidthF

    def getHeightF(self):
        return self.HeightF