import pygame, sys 
from pygame.locals import * 
from pygame import *
import numpy

class Canon():

    def __init__(self, screen,x,y,):
        self.screen = screen
        self.x = x
        self.y = y
        

    def draw(self, mouse_x):
        self.mouse_x = mouse_x

        image = pygame.image.load("CANON.png").convert()
        image = pygame.transform.scale(image, (50, 50))

        if self.mouse_x <= 320:    
            self.angle = 0
        elif self.mouse_x >= 500:
            self.angle = 90
        else:
            self.angle = (self.mouse_x - 320) / 2


        image.set_colorkey((39,190,20))  
        self.screen.blit(pygame.transform.rotate(image, -(self.angle)),(self.x,self.y))
        
        return(self.angle)