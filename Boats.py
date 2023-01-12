import pygame, sys 
from pygame.locals import * 
from pygame import *
import numpy
import random

class Boat():
   
    def __init__(self, lista,):
        self.y = random.randint(250,255)
        self.x = 1000
        self.barcos_lista = lista
        self.size = random.randint(1,5)
        self.barcos_lista.append([self.x , self.y, self.size])

    def lista(self):
        return self.barcos_lista
    
    def spawn_da_boat(screen, lista_barcos, speed):
        image = pygame.image.load("BOAT.png").convert()
        if len(lista_barcos) > 0:
            for lista_barco in lista_barcos:
                lista_barco[0] -= speed
                image.set_colorkey((39,190,20)) 
                if lista_barco[2] == 1:
                    image = pygame.transform.scale(image, (100, 100))
                    screen.blit(image, (lista_barco[0], lista_barco[1] - 25))
                elif lista_barco[2] == 2:
                    image = pygame.transform.scale(image, (120, 120))
                    screen.blit(image, (lista_barco[0], lista_barco[1] - 55))
                elif lista_barco[2] == 3:
                    image = pygame.transform.scale(image, (140, 140))
                    screen.blit(image, (lista_barco[0], lista_barco[1] - 75))
                elif lista_barco[2] == 4:
                    image = pygame.transform.scale(image, (160, 160))
                    screen.blit(image, (lista_barco[0], lista_barco[1] - 85))
                else:
                    image = pygame.transform.scale(image, (180, 180))
                    screen.blit(image, (lista_barco[0], lista_barco[1] - 100))
    