import pygame
from PIL import Image
import random

#Init
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
clock = pygame.time.Clock()




def game_loop():
    game_exit=False
    while not game_exit:
        #event checker

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                print("Quit with event(quit)!")




