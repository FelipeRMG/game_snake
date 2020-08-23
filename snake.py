import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,600)) # Tamanho da Janela
pygame.display.set_caption('SNAKE') # Nome da Janela

while True:

    #Evento para capturar Saída
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update() # Atualiza os frames
