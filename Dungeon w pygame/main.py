import pygame
import time
import random
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
pygame.init()
gameExit=False
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Test')
clock = pygame.time.Clock()

def objectdraw(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def picturedraw(thing,x,y):
    gameDisplay.blit(thing,(x,y))



def gameloop():
    temp=100
    gameExit = False

    while not gameExit:     # Main loop
        gameDisplay.fill(white)
        objectdraw(0,400,800,200,black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                print("Quit with event(quit)!")
            if event.type==pygame.KEYDOWN:   # keydown check
                if event.key == pygame.K_UP:
                   print("asd")
            if event.type == pygame.KEYUP: # Keyrelease check
                if event.key ==pygame.K_UP:
                    print("sad")




        
        pygame.display.update()
        clock.tick(15)

gameloop()
pygame.quit()
quit()
    