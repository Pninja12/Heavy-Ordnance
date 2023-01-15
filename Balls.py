import pygame, sys 
from pygame.locals import * 
import numpy
import time

class Ball():
    def __init__(self,lista, explosion,angle):
        self.x = 20
        self.y = 160
        self.lista_de_balas = lista
        self.gravidade = 0
        self.lista_de_balas.append([self.x , self.y, explosion,angle,self.gravidade])

    def lista(self):
        return self.lista_de_balas

    def disparo(screen, balas_lista):
        image = pygame.image.load("Ball.png").convert()
        if len(balas_lista) > 0:
            for cada_bala in balas_lista:
                cada_bala[0] += (cada_bala[2] * 2) * numpy.sin(numpy.radians(cada_bala[3]))
                cada_bala[1] -= (cada_bala[2] / 2) * numpy.cos(numpy.radians(cada_bala[3])) - cada_bala[4]
                cada_bala[4] += (4.9)/120



                image = pygame.transform.scale(image, (32, 32))
                image.set_colorkey((39,190,20)) 
                screen.blit(image, (cada_bala[0], cada_bala[1])) 