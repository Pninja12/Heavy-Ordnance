import pygame, sys
from pygame.locals import * 
import numpy
import time
import random


#Import dos ficheiros
from Player import Canon
from Boats import Boat
from Balls import Ball


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

#Fontes e texto
myfont = pygame.font.Font('arial.ttf',35)
fontname = pygame.font.Font('arial.ttf',40)
scorefont = pygame.font.Font('arial.ttf',25)
name = fontname.render('Heavy Ordnance' , True , black)
play = myfont.render('Play' , True , black)
quit = myfont.render('Quit' , True , black)

#Imagens
life_image = pygame.image.load("Heart.png").convert()
life_image = pygame.transform.scale(life_image, (32, 32))
life_image.set_colorkey((39,190,20))

image_hold = pygame.image.load("Canon_holder.png").convert()
image_hold = pygame.transform.scale(image_hold, (100, 100))
image_hold.set_colorkey((39,190,20))  

#Variáveis 
jogo = 1                #estado de início de jogo onde roda entro o menu, o jogo e o scoreboard
soma_segundos = 0       #vai somando 1 cada vez que o programa repete-se, já que o mesmo corre 60 vezes em um segundo
boats_on_game = []      #lista do barcos presentes no jogo
speed = 0.5             #velocidade de todos os barcos
barco_destruido = 0     #vai somando cada vez que um barco é destruído para ir adicionar ao speed e ao multiplayer
multiplier = 1          #adiciona valores ao scoreboard
charging = 0            #variável de lock para verificar se o rato está a ser pressionado
segundos = 0            #variável que obtem o valor de segundos desde que o jogo começou
mouse_up = 0            #variável que verifica se o rato foi largado
balls_on_game = []      #lista das balas de canhão no jogo
time_write = 0          #variável de lock que só desbloqueia quando o player tem de escrever o seu nome
player_score = []       #lista do que é do nome do jogador
best_score = []         #lista dos melhores resultados do ficheiro






while True:
    clock = pygame.time.Clock()                     #recebe a função 
    mouse_press = pygame.mouse.get_pressed()        #recebe se o rato está a ser clicado
    keys=pygame.key.get_pressed()                   #recebe quais as teclas é que estão a ser clicadas
    screen.fill((159,237,223))
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        if keys[K_ESCAPE]:
            pygame.quit() 
            sys.exit()
        if jogo == 1 and mouse_press[0] and ((mouse_xy[0] >= 250 and mouse_xy[0] <= 325) and (mouse_xy[1] >= 110 and mouse_xy[1] <= 145)):          #quando o jogo começa coloca tudo em números neutros
            jogo = 2
            life = 3
            segundos = 0
            score = 0
            soma_segundos = 0
            next_boat = 0
            lock = 0
            charging = -4
            working = 0
            mouse_up = 0
            explosion = 0
            spawn_da_ball = 0
            multiplier = 1
            speed = 0.5
            time_write = 0
            one_time = 0
            last_thing = 0
            player_score = []
            best_score = []
        if jogo == 1 and mouse_press[0] and ((mouse_xy[0] >= 250 and mouse_xy[0] <= 325) and (mouse_xy[1] >= 150 and mouse_xy[1] <= 185)):
            pygame.quit() 
            sys.exit()
        if (event.type == pygame.MOUSEBUTTONUP or charging + 3 == segundos) and segundos >= 2 :
            mouse_up = 1
        if time_write == 1 and keys[K_a] and len(player_score) < 3:
            player_score.append('a')
        if time_write == 1 and keys[K_b] and len(player_score) < 3:
            player_score.append('b')
        if time_write == 1 and keys[K_c] and len(player_score) < 3:
            player_score.append('c')
        if time_write == 1 and keys[K_d] and len(player_score) < 3:
            player_score.append('d')
        if time_write == 1 and keys[K_e] and len(player_score) < 3:
            player_score.append('e')
        if time_write == 1 and keys[K_f] and len(player_score) < 3:
            player_score.append('f')
        if time_write == 1 and keys[K_g] and len(player_score) < 3:
            player_score.append('g')
        if time_write == 1 and keys[K_h] and len(player_score) < 3:
            player_score.append('h')
        if time_write == 1 and keys[K_i] and len(player_score) < 3:
            player_score.append('i')
        if time_write == 1 and keys[K_j] and len(player_score) < 3:
            player_score.append('j')
        if time_write == 1 and keys[K_k] and len(player_score) < 3:
            player_score.append('k')
        if time_write == 1 and keys[K_l] and len(player_score) < 3:
            player_score.append('l')
        if time_write == 1 and keys[K_m] and len(player_score) < 3:
            player_score.append('m')
        if time_write == 1 and keys[K_n] and len(player_score) < 3:
            player_score.append('n')
        if time_write == 1 and keys[K_o] and len(player_score) < 3:
            player_score.append('o')
        if time_write == 1 and keys[K_p] and len(player_score) < 3:
            player_score.append('p')
        if time_write == 1 and keys[K_q] and len(player_score) < 3:
            player_score.append('q')
        if time_write == 1 and keys[K_r] and len(player_score) < 3:
            player_score.append('r')
        if time_write == 1 and keys[K_s] and len(player_score) < 3:
            player_score.append('s')
        if time_write == 1 and keys[K_t] and len(player_score) < 3:
            player_score.append('t')
        if time_write == 1 and keys[K_u] and len(player_score) < 3:
            player_score.append('u')
        if time_write == 1 and keys[K_v] and len(player_score) < 3:
            player_score.append('v')
        if time_write == 1 and keys[K_w] and len(player_score) < 3:
            player_score.append('w')
        if time_write == 1 and keys[K_x] and len(player_score) < 3:
            player_score.append('x')
        if time_write == 1 and keys[K_y] and len(player_score) < 3:
            player_score.append('y')
        if time_write == 1 and keys[K_z] and len(player_score) < 3:
            player_score.append('z')
        if time_write == 1 and keys[K_BACKSPACE] and len(player_score) != 0:
            player_score.pop(len(player_score) - 1)
        if time_write == 1 and keys[K_RETURN] and len(player_score) == 3:
            time_write = 0
            highscore_data = [score," ",player_score]
            with open("highscore.txt", "a") as file:        #abre o ficheiro do scoreboard e adiciona o score e nome do jogador
                file.write(str(score))
                file.write(str(" "))
                for i in range(len(player_score)):
                    file.write(str(player_score[i]))
                file.write("\n")
            file.close()
            last_thing = 1
            
    
    if (mouse_up == 1 or charging + 3 == segundos) and len(balls_on_game) < 2:          #verifica quanto tempo o rato ficou pressionado para dizer à bola o quanto deve viajar e adiciona a bola à sua lista respectível
        mouse_up = 0
        working = 0
        balls_on_game = Ball(balls_on_game, explosion,angle).lista()
        if charging == segundos:
            explosion = 1
        elif charging + 1 == segundos:
            explosion = 2
        elif charging + 2 == segundos:
            explosion = 3
        else:
            explosion = 4
        charging = 0
        



    mouse_xy = []
    mouse_xy = pygame.mouse.get_pos()
    mouse_press = []
    mouse_press = pygame.mouse.get_pressed()


    jogador = Canon(screen, 12, 150)        #indica onde o canhão vai ficar no ecrã
    

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
    elif jogo == 2 and life > 0:

        angle = jogador.draw(mouse_xy[0])  #desenha o canhão que o jogador controla no ecrã

        for i in range(life):
            screen.blit(life_image , ((900 + i * 30), 30))          #desenha os corações a simbolizar a vida, as vezes necessárias

        score_text = scorefont.render("score ->" , True , (0,0,0))
        score_number = scorefont.render(f"{score}" , True , (0,0,0))
        screen.blit(score_text, (805, 0))
        screen.blit(score_number, (903, 0))


        pygame.draw.rect(screen, green, pygame.Rect(0, 190, 100, 190))          #desenha a parte verde
        pygame.draw.rect(screen, orange, pygame.Rect(100, 315, 100, 125))       #desenha a parte laranja
        pygame.draw.rect(screen, blue, pygame.Rect(200, 315, 800, 125))         #desenha a parte azul
        
        
        if soma_segundos == 60:     #traduz todas as vezes que o programa rodou para um segundo
            segundos += 1
            soma_segundos = 0
            score += 1

        if len(boats_on_game) < 4 and lock == 0:        #verifica que só há 4 barcos no jogo
            next_boat += random.randint(1,10)
            lock = 1

        if next_boat <= segundos and lock == 1:         #chama a função de barcos e adiciona na respetiva lista
            next_boat = segundos
            boats_on_game = Boat(boats_on_game).lista()
            lock = 0

        if barco_destruido == 10:           #se 10 barcos forem destruidos aumenta o speed e o multiplier
            barco_destruido = 0
            multiplier += 1
            speed += 0.5
        
        cont_barco = 0
        for where_boat in boats_on_game:            #verifica se os barcos estão na zona laranja e os destrói tirando uma vida
            if where_boat[0] <= 200:
                boats_on_game.pop(cont_barco)
                life -= 1
            cont_barco +=1

        if working == 0:                #forma de verificar se o rato está a ser pressionado
            if mouse_press[0]:
                charging = segundos
                working = 1
        
        
        cont_balls = 0
        for where_balls in balls_on_game:                   #verifica se as balas caíram na água ou se tocaram no barco para serem destruidas e acontecer o que está no enunciado
            if where_balls[1] >= 350:
                balls_on_game.pop(cont_balls)

            balls_col = pygame.Rect(where_balls[0], where_balls[1], 10, 10)
            
            
            
            cont_barco = 0
            for where_boat in boats_on_game:
                boats_col = pygame.Rect(where_boat[0], where_boat[1], where_boat[0] + 75, where_boat[1])
                collide = boats_col.colliderect(balls_col)
                if collide:
                    score += where_boat[2] * multiplier
                    boats_on_game.pop(cont_barco)
                    if len(balls_on_game) > 0:
                        balls_on_game.pop(cont_balls)
                    barco_destruido += 1
                    
                cont_barco +=1
            cont_balls +=1

        Boat.spawn_da_boat(screen,boats_on_game,speed)          #desenha os barcos 

        Ball.disparo(screen, balls_on_game)                     #desenha as bolas


        screen.blit(image_hold,(-10,90))                        #desenha o que está a segurar o canhão
        one_time = 1
        time_write = 1
    else: 
        

        cont_barco = 0
        for where_boat in boats_on_game:            #apaga todos os barcos
            boats_on_game.pop(cont_barco)
            cont_barco +=1
        
        cont_balls = 0
        for where_balls in balls_on_game:           #apaga todas as bolas
            balls_on_game.pop(cont_balls)
            cont_balls +=1
        
        if one_time == 1:                           #aparece o ecrã de game over
            gameover = fontname.render("Game Over!" , True , (0,0,0))
            screen.blit(gameover , (400, 50))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(3)
            one_time = 0
            

        name_name = fontname.render("Como te chamas:" , True , (0,0,0))         #perguntar o nome do jogador
        holder = fontname.render("_" , True , (0,0,0))
        screen.blit(name_name , (330, 50))
        for i in range(3):
            screen.blit(holder, (400 + i * 50, 150))
            
        for i in range(len(player_score)):
            score_letter = fontname.render(f"{player_score[i]}" , True , (0,0,0))
            screen.blit(score_letter, (400 + i * 50, 130))
        
        if last_thing == 1:                 #abre o ficheiro e recebe todas as pontuações para mostrar as 3 melhores
            with open("highscore.txt", "r") as file:
                for line in file:

                    # reading each word 
                    numbers_highscore = 0
                    letter_highscore = ""
                    after_number = 0       
                    for word in line.split():
                        if after_number == 0:
                            numbers_highscore = word
                            after_number = 1
                        else:
                            letter_highscore = word
                    best_score.append([int(numbers_highscore),letter_highscore])
            file.close()
            best_score.sort(reverse=True) 
            screen.fill((159,237,223))
            best_score1 = myfont.render(str(best_score[0]) , True , (0,0,0))
            best_score2 = myfont.render(str(best_score[1]) , True , (0,0,0))
            best_score3 = myfont.render(str(best_score[2]) , True , (0,0,0))
            highscore_text = fontname.render("Highscore" , True , (0,0,0))
            screen.blit(highscore_text , (400, 50))
            screen.blit(best_score1 , (400, 100))
            screen.blit(best_score2 , (400,150))
            screen.blit(best_score3 , (400,200))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            jogo = 1




    
    
    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    soma_segundos += 1
    



#Referências
"""
https://coderslegacy.com/python/display-fps-pygame/
https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
https://coderslegacy.com/python/pygame-mouse-click/
https://www.reddit.com/r/pygame/comments/7y8yao/how_to_detect_mouse_release/
https://stackoverflow.com/questions/26811132/pygame-keyup-keydown

"""


