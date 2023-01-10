import pygame, sys 
from pygame.locals import * 
from pygame import *
import numpy

class Canon():

    def __init__(self, screen,angle,x,y):
        self.screen = screen
        self.keys = pygame.key.get_pressed()
        self.angle = angle
        self.timegame = 0
        self.x = x
        self.y = y

    def draw(self):
        
        image = pygame.image.load("CANON.png").convert()
        image = pygame.transform.scale(image, (50, 50))
        image = pygame.transform.rotate(image, self.angle)
        
        
        if self.keys[pygame.K_LEFT]:
            self.angle += 0.25
        if self.keys[pygame.K_RIGHT]:
            self.angle -= 0.25
        if self.keys[pygame.K_UP]:
            if self.speed > -0.5:                                  
                self.speed -= 0.01
        if self.keys[pygame.K_DOWN]:
            if self.speed < 0:                                   
                self.speed += 0.0005
        if not self.keys[pygame.K_UP]:                           
            if self.speed < 0:                                   
                self.speed += 0.0005
        if self.speed > 0:                                       
            self.speed = 0 

        if self.angle >= 360:
            self.angle = 0
        if self.angle <= -360:
            self.angle = 0

        self.y -= numpy.sin(numpy.radians(self.angle * 2))      
        self.x += numpy.cos(numpy.radians(self.angle * 2))
        rot_image = pygame.transform.rotate(image, (self.angle + 90))
        rot_image.set_colorkey((39,190,20))  
        
        self.screen.blit(image,(100,100))
        
    
        return(self.angle,self.speed, self.x, self.y)