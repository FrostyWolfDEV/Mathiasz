import pygame
import random
from PIL import Image
import os
pygame.init
pygame.font.init()
display_width = 1600
display_height = 900
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pygame Test')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue=(0,0,255)
green=(0,255,0)
Bground=pygame.image.load("bg4.png")


def imgplace(image,x,y):
    gameDisplay.blit(image,(x,y))
def pointer(color,thingx,thingy,radius):
    pygame.draw.circle(gameDisplay, color, [thingx, thingy],radius )
def drawsquare(color,x,y,width,height):
    pygame.draw.rect(gameDisplay,color,[x,y,width,height])

def drawer(places,colors):
    counter=-1
    for listas in places:
        x=listas[0]
        y=listas[1]
        counter+=1
        pointer(colors[counter],x,y,10)
def getquestion(usedszam):
    kerdesek=open("questions.txt","r", encoding="UTF-8")
    szam=random.randint(1,3)
    counter=0
    end=0
    print(szam)
    
    while end!=1 and counter<1000:
        if szam not in usedszam:
            for i in range(szam):
                vegso=kerdesek.readline()
            vegso=vegso[:-1]
            returnlist=[vegso,usedszam]
            usedszam.append(szam)
            return(returnlist)
        else:
            szam=random.randint(1,3)
        counter+=1
    if counter>=1000:
        returnlist=["Out of questions error!",usedszam]
        return(returnlist)
    
    







def game_loop():
    x=400
    y=400
    xchange=0
    ychange=0
    gameExit=False
    places=[]
    colors=[]
    colorcounter=0
    colorset=[red,green,blue,white]
    font = pygame.font.SysFont('timesnewroman',  30)
    usedszam=[]
    questionreturn=getquestion(usedszam)
    question=questionreturn[0]
    usedszam=questionreturn[1]

    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                print("Quit with event(quit)!")

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    xchange=-10
                if event.key==pygame.K_RIGHT:
                    xchange=10
                if event.key==pygame.K_UP:
                    ychange=-10
                if event.key== pygame.K_DOWN:
                    ychange=10
                if event.key==pygame.K_s:
                    temp=[x,y]
                    places.append(temp)
                    colors.append(colorset[colorcounter])
                    if colorcounter<3:
                        colorcounter+=1
                    else:
                        colorcounter=0
                if event.key == pygame.K_RETURN:
                    questionreturn=getquestion(usedszam)
                    usedszam=questionreturn[1]
                    question=questionreturn[0]
                    
                    
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange=0
                if event.key ==pygame.K_UP or event.key== pygame.K_DOWN:
                    ychange=0

        x+=xchange
        y+=ychange
        
        text = font.render(question, True, red, None)
        textRect = text.get_rect()
        textRect.center = (display_width // 2, display_height-55 )

        imgplace(Bground,0,0)
        
        pointer(black,x,y,20)
        drawer(places,colors)
        drawsquare(black,0,display_height-80,display_width,70)
        gameDisplay.blit(text, textRect)
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()