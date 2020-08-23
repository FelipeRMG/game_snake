import pygame, random
from pygame.locals import *

# Direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT =3

pygame.init()
screen = pygame.display.set_mode((600,600)) # Tamanho da Janela
pygame.display.set_caption('SNAKE') # Nome da Janela

snake = [(200,200),(210,200),(220,200)] #define o deslocamento
snake_skin = pygame.Surface((10,10))# define o tamanho
snake_skin.fill((0,250,0))# define a cor

apple_skin = pygame.Surface((10,10))
apple_skin.fill((255,0,0))
apple_pos = (random.randint(0,590), random.randint(0,590))

my_direction = LEFT

clock = pygame.time.Clock()

while True:

    clock.tick(20) # limita o FPS
    #Evento para capturar Saída
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        #captura de teclado
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    # Movimentação
    if my_direction == UP: # deslocamento para cima
        snake[0] = (snake[0][0],snake[0][1] - 10)
    if my_direction == DOWN: # deslocamento para cima
        snake[0] = (snake[0][0],snake[0][1] + 10)
    if my_direction == LEFT: # deslocamento para cima
        snake[0] = (snake[0][0] - 10,snake[0][1])
    if my_direction == RIGHT: # deslocamento para cima
        snake[0] = (snake[0][0] + 10,snake[0][1])

    # Atualiza o corpo da cobra
    for i in range(len(snake) - 1, 0, -1):
        snake [i] = (snake[i-1][0], snake[i-1][1]) # recebe a posição anterior

    screen.fill((0,0,0))
    screen.blit(apple_skin,apple_pos)
    for snake_pos in snake:
        screen.blit(snake_skin,snake_pos)

    pygame.display.update() # Atualiza os frames
