import pygame, sys 
from pygame.locals import * 
from pygame import *
import numpy

class Canon():

    def __init__(self, screen,x,y,):
        self.screen = screen
        self.x = x
        self.y = y
        

    def draw(self, mouse_y):
        self.mouse_y = mouse_y

        image = pygame.image.load("CANON.png").convert()
        image = pygame.transform.scale(image, (50, 100))

        if self.mouse_y <= 120:    
            self.angle = 0
        elif self.mouse_y >= 300:
            self.angle = 90
        else:
            self.angle = (self.mouse_y - 120) / 2
            print(-((self.mouse_y - 120) / 2))


        rot_image = pygame.transform.rotate(image, -(self.angle))
        rot_image.set_colorkey((39,190,20))  
        self.screen.blit(rot_image,(self.x,self.y))
        
        return(self.angle)