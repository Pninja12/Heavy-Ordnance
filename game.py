import pygame, sys
from pygame.locals import * 
import numpy
import time
import random

pygame.init()

current_time = []
jogo = 1
myfont = pygame.font.Font('arial.ttf',35)
fontname = pygame.font.Font('arial.ttf',40)
name = fontname.render('Heavy Ordnance' , True , (0,0,0))

keys=pygame.key.get_pressed()
screen = pygame.display.set_mode((1000, 380)) 
pygame.display.set_caption("Heavy Ordnance") 

while True:
    screen.fill((159,237,223))
    current_time.append(time.gmtime()[3])
    current_time.append(time.gmtime()[4])  
    current_time.append(time.gmtime()[5])
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        if keys[K_ESCAPE]:
            pygame.quit() 
            sys.exit()
         
    if jogo == 1:
        screen.blit(name , (250,50))


    pygame.display.update()
    
    