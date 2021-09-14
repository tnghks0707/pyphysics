import pygame

class Object:
    Surface: pygame.Surface
    Rect: pygame.Rect

    def __init__(self, Isurface):
        self.Surface = Isurface
        self.Rect = self.Surface.get_rect()

class Rigidbody:
    Mass = 0.0
    HeightF = 0.0
    HeightV = 0.0
    HeightA = 0.0
    def __init(self, ):
        pass