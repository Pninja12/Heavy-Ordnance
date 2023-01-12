import pygame, sys
from pygame.locals import * 
import numpy
import time
import random


#Import dos ficheiros
from Player import Canon
from Boats import Boat


pygame.init()
screen = pygame.display.set_mode((1000, 380)) 
pygame.display.set_caption("Heavy Ordnance") 


#colors
black = (0,0,0)
purple = (180, 128, 242)
orange = (250, 100, 0)
red = (240,20,20)
green = (20,240,20)
blue = (20,20,240)


current_time = []
jogo = 1
myfont = pygame.font.Font('arial.ttf',35)
fontname = pygame.font.Font('arial.ttf',40)
scorefont = pygame.font.Font('arial.ttf',25)
name = fontname.render('Heavy Ordnance' , True , black)
play = myfont.render('Play' , True , black)
quit = myfont.render('Quit' , True , black)
soma_segundos = 0
life_image = pygame.image.load("Heart.png").convert()
life_image = pygame.transform.scale(life_image, (32, 32))
life_image.set_colorkey((39,190,20))
boats_on_game = []
speed = 0.5
barco_destruido = 0
multiplier = 0
image_hold = pygame.image.load("Canon_holder.png").convert()
image_hold = pygame.transform.scale(image_hold, (100, 100))
image_hold.set_colorkey((39,190,20))  

clock = pygame.time.Clock()
mouse_press = pygame.mouse.get_pressed()
keys=pygame.key.get_pressed()


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
        if jogo == 1 and mouse_press[0] and ((mouse_xy[0] >= 250 and mouse_xy[0] <= 325) and (mouse_xy[1] >= 110 and mouse_xy[1] <= 145)):
            jogo = 2
            life = 3
            segundos = 0
            score = 0
            soma_segundos = 0
            next_boat = 0
            lock = 0
        if jogo == 1 and mouse_press[0] and ((mouse_xy[0] >= 250 and mouse_xy[0] <= 325) and (mouse_xy[1] >= 150 and mouse_xy[1] <= 185)):
            pygame.quit() 
            sys.exit()
         


    mouse_xy = []
    mouse_xy = pygame.mouse.get_pos()
    mouse_press = []
    mouse_press = pygame.mouse.get_pressed()


    jogador = Canon(screen, 12, 150)
    

    #Menu do jogo
    if jogo == 1:
        screen.blit(name , (250,50))
        if (mouse_xy[0] >= 250 and mouse_xy[0] <= 325) and (mouse_xy[1] >= 110 and mouse_xy[1] <= 145):
            pygame.draw.rect(screen, purple, pygame.Rect(250, 110, 100, 40))

        if (mouse_xy[0] >= 250 and mouse_xy[0] <= 325) and (mouse_xy[1] >= 150 and mouse_xy[1] <= 185):
            pygame.draw.rect(screen, purple, pygame.Rect(250, 150, 100, 40))
        
        screen.blit(play , (250,110))
        screen.blit(quit , (250,150))
        screen.blit(name , (250,50))




    #Jogo
    if jogo == 2 and life > 0:

        angle = jogador.draw(mouse_xy[0])

        for i in range(life):
            screen.blit(life_image , ((900 + i * 30), 30))

        score_text = scorefont.render("score ->" , True , (0,0,0))
        score_number = scorefont.render(f"{score}" , True , (0,0,0))
        screen.blit(score_text, (805, 0))
        screen.blit(score_number, (903, 0))


        pygame.draw.rect(screen, green, pygame.Rect(0, 190, 100, 190))
        pygame.draw.rect(screen, orange, pygame.Rect(100, 315, 100, 125))
        pygame.draw.rect(screen, blue, pygame.Rect(200, 315, 800, 125))
        
        
        if soma_segundos == 60:
            segundos += 1
            soma_segundos = 0
            score += 1

        if len(boats_on_game) < 4 and lock == 0:
            next_boat += random.randint(1,10)
            lock = 1

        if next_boat == segundos and lock == 1:
            next_boat = segundos
            boats_on_game = Boat(boats_on_game).lista()
            lock = 0

        if barco_destruido == 10:
            barco_destruido = 0
            multiplier += 1
            speed += 1
        
        cont_barco = 0
        for where_boat in boats_on_game:
            if where_boat[0] <= 200:
                boats_on_game.pop(cont_barco)
                life -= 1
            cont_barco +=1


        Boat.spawn_da_boat(screen,boats_on_game,speed)


        screen.blit(image_hold,(-10,90))
    else: 
        
        
        

        cont_barco = 0
        for where_boat in boats_on_game:
            boats_on_game.pop(cont_barco)
            cont_barco +=1
        
        
        jogo = 1
        


    #retirar no fim
    mouse_pos = myfont.render(f"[{mouse_xy[0]},{mouse_xy[1]}]" , True , (0,0,0))
    #retirar no fim




    screen.blit(mouse_pos , (mouse_xy[0] + 10,mouse_xy[1] + 10))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    soma_segundos += 1
    


#Referências
"""
https://coderslegacy.com/python/display-fps-pygame/
https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
https://coderslegacy.com/python/pygame-mouse-click/

"""



#to do
"""
verificar velocidade
clicar para disparar
adicionar balas
gravidade nas balas
"""