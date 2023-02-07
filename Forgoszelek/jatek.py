import pygame
import random
from PIL import Image
import os
import sys      # Warning! Just a failsafe! Don't touch! EVER! 
pygame.init
pygame.font.init()
display_width = 1600
display_height = 900
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Forgószelek by:ForstyWolfDEV')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue=(0,0,255)
green=(0,255,0)
Bground=pygame.image.load("bg4.png")

def loadfromlong():   #Read from long term memory
    longstorage=open("save_long.txt","r")
    end=0
    colorinfo=""
    cords=""
    while end!=1:
        temp=longstorage.readline()
        if "<end>" not in temp:
            templist=list(temp)
            atdivide=False
            counter=0
            while not atdivide:
                if templist[counter]!="&":
                    colorinfo=colorinfo+templist[counter]
                    counter+=1
                    if counter>1000:
                        sys.exit() #failsafe becouse of infinite loop possibility (Mintha kihúznád az áramot)
                else:
                    atdivide=True
                    counter+=1
            while templist[counter-1]!="]":
                cords=cords+templist[counter]
                counter+=1
                if counter>1000:
                        sys.exit() #failsafe becouse of infinite loop possibility (Mintha kihúznád az áramot)

        else:
            
            end=1
            returnready=[colorinfo,cords]
            return (returnready)


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
def getquestion(usedszam):  #Question chooser
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
        

def game_loop(): # Main loop 
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

    spread=loadfromlong()
    colors=spread[0]
    places=[spread[1]]
    print(colors)
    print(places)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit + save dots to long term
                gameExit = True
                print("Quit with event(quit)!")
                counter=0
                save=open("save.txt","w")
                for i in colors:
                    
                    save.write(str(i)+"&"+str(places[counter])+"\n")
                    counter+=1
                save.close()
        

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    xchange=-10
                if event.key==pygame.K_RIGHT:
                    xchange=10
                if event.key==pygame.K_UP:
                    ychange=-10
                if event.key== pygame.K_DOWN:
                    ychange=10
                if event.key==pygame.K_s:  # Save dots in local 
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

        imgplace(Bground,0,0)  # Background
        
        pointer(black,x,y,20)
        drawer(places,colors)
        drawsquare(black,0,display_height-80,display_width,70)
        gameDisplay.blit(text, textRect)
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()