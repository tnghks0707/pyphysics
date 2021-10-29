import pygame
import PyphyTypes
import importlib
import os

class Object:
    Name: str
    Surface: pygame.Surface
    Rect: pygame.Rect
    rigidbody = None
    Visible = True
    UserScriptEnable = False
    UserScript = None
    UserScriptPath = None

    def __init__(self, Isurface, rect=None, name=None, size=None, visible=True, UserScript: str = None):
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
            self.Rect.size = size
            #self.Rect = self.Surface.get_rect()
        if UserScript != None:
            self.UserScriptPath = UserScript
            UserScript =  os.path.splitext(UserScript)[0]
            excepted = False
            try:
                self.UserScript = importlib.import_module(UserScript)
            except Exception:
                excepted = True
                print(name + " : Error importing user script \"" + UserScript + "\"!")
            if excepted == False:
                self.UserScriptEnable = True
        

    def SetRigidbody(self, mass, Fz_x = False, Fz_y = False):
        self.rigidbody = Rigidbody(self.Rect, mass)
        self.rigidbody.freeze_x = Fz_x
        self.rigidbody.freeze_y = Fz_y

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
    
    WidthF = 0.0
    WidthA = 0.0
    WidthDeltaA = 0.0
    WidthDistence = 0.0
    
    freeze_x = False
    freeze_y = False

    def __init__(self, Rect: pygame.Rect, mass, Fz_x = False, Fz_y = False):
        self.Rect = Rect
        self.Mess = mass
        (self.WidthDistence, self.HeightDistence) = Rect.topleft
        self.freeze_x = Fz_x
        self.freeze_y = Fz_y

    def SetSpeed(self, vector):
        if self.freeze_x == False:
            self.WidthDeltaA = vector.getWidthF()
        if self.freeze_y == False:
            self.HeightDeltaA = vector.getHeightF()

    def AddForce(self, vector):
        if self.freeze_x == False:
            self.WidthF += vector.getWidthF()
        if self.freeze_y == False:
            self.HeightF += vector.getHeightF()

    def AddWidthMomentum(self, p):#p = mv v = p/m
        if self.freeze_x == False:
            self.WidthDeltaA = p / self.Mess * -1

    def AddHeightMomentum(self, p):
        if self.freeze_y == False:
            self.HeightDeltaA = p / self.Mess

    def GetWidthMomentum(self):
        return self.Mess * self.WidthDeltaA * -1

    def GetHeightMomentum(self):
        return self.Mess * self.HeightDeltaA

    def Calculate(self, timeDelta):
        self.HeightA = self.HeightF / self.Mess
        self.HeightF = 0

        self.WidthA = self.WidthF / self.Mess
        self.WidthF = 0

        timedelta_f = timeDelta / 1000
        #지속시간에 더함
        #timecontinue += timedelta_f

        self.HeightDeltaA += self.HeightA * timedelta_f
        self.HeightDistence -= self.HeightDeltaA * timedelta_f * 100

        self.WidthDeltaA += self.WidthA * timedelta_f
        self.WidthDistence -= self.WidthDeltaA * timedelta_f * 100

        self.Rect.topleft = (self.WidthDistence, self.HeightDistence)

        #print(self.HeightDeltaA)

        if(self.HeightDistence > 1000):
            self.HeightDistence = -500

        if(self.HeightDistence < -1000):
            self.HeightDistence = 900

        if(self.WidthDistence > 1400):
            self.WidthDistence = -500

        if(self.WidthDistence < -500):
            self.WidthDistence = 1300



class Vector:
    HeightF = 0.0
    WidthF = 0.0
    
    def __init__(self, WidthF, HeightF):
        self.HeightF = HeightF
        self.WidthF = WidthF * -1

    def getHeightF(self):
        return self.HeightF

    def getWidthF(self):
        return self.WidthF
