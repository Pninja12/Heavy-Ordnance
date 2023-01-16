# Heavy-Ordnance
# Projeto de Iniciação à Computação
### Relatório

![Imagem com piratas e canhões](https://media.istockphoto.com/id/1151906766/vector/pirate-ship-flat-vector-illustration.jpg?s=612x612&w=0&k=20&c=bbtpr-VArxDDdOROzctE3kNa9phBYeKXlkBz1NFy6IA=)

### [Repositório GitHub](https://github.com/Pninja12/Heavy-Ordnance)

## Quem fez e o quê
- Paulo Silva (22206205)
    - Lógica do jogo
- Mariana Marques (22207510)
    - Ficheiro Markdown

---

## Pontuação Extra

[ ] Sistema de Audio
[ ] Sistema de "Power-Ups"
[ ] Sistema de Particulas
[ ] Graficos e Animações mais complexas

---

## Lógica do código

1. ##### Objetos
    - Cada objeto tem um ficheiro próprio
    - Os barcos e as bolas do canhão são adicionados para uma lista para depois serem desenhados

2. ##### Ciclos
    - O jogo tem 3 estados
    - O 1º estado refere-se ao menu
    - O 2º estado refere-se ao desenvolvimento do jogo
    - O 3º estado refere-se ao fim do jogo, a adição do score do jogador à leaderboard e a amostra dos 3 melhores

4. ##### Import's
    - O "import pygame, sys" vai importar tudo o que tem a ver com o pygame
    - O "from pygame.locals import *" 
    - O "import numpy" vai importar todas as funções matemáticas
    - O "import time" vai importar as funções do tempo
    - O "import random" vai importar as funções de números aleatórios
    - O "from Player import Canon" vai importar o canhão que o jogador usa
    - O "from Boats import Boat" vai importar os barcos
    - O "from Balls import Ball" vai importar as bolas do canhão

5. ##### Pensamento Lógico
    - O jogo começa com o menu que quando é clicado o butão de "Jogar" todas as variáveis usadas no jogo retornam aos seus valores iniciais
    - Todos os barcos e bolas são guardados em listas que são chamadas mais tarde para desenhar os mesmos
    - O jogo só roda 60 em um segundo por isso há uma veriável que quando chega a 60, volta a zero e adiciona um em segundos o que faz com que possa usar isso como medida de tempo

6. ##### Informação usada de fora
    - Site [Coders Legacy](https://coderslegacy.com/python/display-fps-pygame/)
    - Site [Geeks for Geeks](https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/)
    - Site [Coders Legacy](https://coderslegacy.com/python/pygame-mouse-click/)
    - Site [Reddit](https://www.reddit.com/r/pygame/comments/7y8yao/how_to_detect_mouse_release/)
    - Site [Stackoverflow](https://stackoverflow.com/questions/26811132/pygame-keyup-keydown)
    - Outro trabalho [Github](https://github.com/Pninja12/Pew-Pew-Comets)
    - Colegas:
        | Nome | Número | Ajuda |
        | - | - | - |
        | António Rodrigues | 22202884 | Lógica do jogo rodar apenas 60 vezes em 1 segundo |