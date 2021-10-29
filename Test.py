from pygame import Rect
import PyphyObject
import pygame
from pygame.locals import *

def Update(Object: PyphyObject.Object, pygame: pygame):
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        Object.rigidbody.AddForce(PyphyObject.Vector(-5, 0))
    if keys[K_RIGHT]:
        Object.rigidbody.AddForce(PyphyObject.Vector(5, 0))
    if keys[K_UP]:
        Object.rigidbody.AddForce(PyphyObject.Vector(0, 25))
    if keys[K_UP]:
        Object.rigidbody.AddForce(PyphyObject.Vector(0, -5))
    if keys[K_SPACE]:
        Object.rigidbody.SetSpeed(PyphyObject.Vector(0, 0))