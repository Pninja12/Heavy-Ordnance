import pygame, sys 
from pygame.locals import * 
from pygame import *
import numpy

class Boat():
   
    def __init__(self, lista):
        self.y = 315
        self.x = 1000
        self.barcos_lista = lista
        self.barcos_lista.append([self.x , self.y])

    def lista(self):
        return self.barcos_lista
    
    def spawn_da_boat(screen, lista_barcos, speed):
        image = pygame.image.load("BOAT.png").convert()
        if len(lista_barcos) > 0:
            for lista_barco in lista_barcos:
                lista_barco[0] -= speed
                image.set_colorkey((39,190,20)) 
                
                print(lista_barco[0], lista_barco[1])
                screen.blit(image, (lista_barco[0], lista_barco[1])) 
    
