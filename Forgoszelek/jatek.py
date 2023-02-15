import pygame
import random
from PIL import Image

import os
import sys      # Warning! Just a failsafe! Don't touch! EVER! 
import ast      # Used to convert str to list when reading from save
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
    cordsbreakdown=""
    cordsreadylist=[]
    colorsreadylist=[]
    colorsdreakdown=""
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
            
            for i in cords: # Reconstruct cords to make it usable plus puts it into a list
                cordsbreakdown=cordsbreakdown+i
                if i=="]":
                    cordsok=ast.literal_eval(cordsbreakdown)
                    cordsreadylist.append(cordsok)
                    cordsbreakdown=""
                    cordsok=""

            for i in colorinfo: # Reconstruct colors to make it usable plus puts it into a list
                colorsdreakdown=colorsdreakdown+i
                if i==")":
                    colorsok=ast.literal_eval(colorsdreakdown)
                    colorsreadylist.append(colorsok)
                    colorsdreakdown=""
                    colorsok=""

            #colorinfo2= ast.literal_eval(colorinfo)  # CRASH!!
            #cords2= ast.literal_eval(cords)          # CRASH!!
            returnready=[cordsreadylist,colorsreadylist]
            print(returnready)
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
        


def buffercheck(buffer,bufferstate,colors,colorset):      # REALLLLLLY UNDERTESTED! (Should work fine.(Maybe))
    if bufferstate=="":
        bufferstate=buffer
        buffer=""
    else:
        try:
            
            colors[int(bufferstate)]=colorset[int(buffer)]
            bufferstate=""
            buffer=""
        except:
            print("Except error caught!")
            bufferstate=""
            buffer=""

        
    returnready=[buffer,bufferstate,colors]
    return returnready


def game_loop(): # Main loop #################################### MAIN GAME FROM DOWN HERE! ################################
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
    buffer=""
    bufferstate=""
    spread=loadfromlong()
    colors=spread[1]
    places=spread[0]
    turn=0
    checkok=False
    
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
                if event.key == pygame.K_q:
                    questionreturn=getquestion(usedszam)
                    usedszam=questionreturn[1]
                    question=questionreturn[0]
                    turn+=1
                if event.key==pygame.K_0:   # ############## Buffer Setup #############
                    buffer=buffer+"0"
                if event.key==pygame.K_1:
                    buffer=buffer+"1"
                if event.key==pygame.K_2:
                    buffer=buffer+"2"
                if event.key==pygame.K_3:
                    buffer=buffer+"3"
                if event.key==pygame.K_4:
                    buffer=buffer+"4"
                if event.key==pygame.K_5:
                    buffer=buffer+"5"
                if event.key==pygame.K_6:
                    buffer=buffer+"6"
                if event.key==pygame.K_7:
                    buffer=buffer+"7"
                if event.key==pygame.K_8:
                    buffer=buffer+"8"
                if event.key==pygame.K_9:
                    buffer=buffer+"9"
                if event.key==pygame.K_r:
                    buffer=""
                    bufferstate=""
                if event.key==pygame.K_RETURN:
                    bufferin=buffercheck(buffer,bufferstate,colors,colorset)
                    buffer=bufferin[0]
                    bufferstate=bufferin[1]
                    colors=bufferin[2]
                    

                    
                    
            if event.type ==pygame.KEYUP:   
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange=0
                if event.key ==pygame.K_UP or event.key== pygame.K_DOWN:
                    ychange=0

        x+=xchange
        y+=ychange
        
        text = font.render(question, True, red, None)
        text2= font.render(str(turn)+"/30",True,red,None)
        textRect = text.get_rect()
        textRect2=text2.get_rect()
        textRect.center = (display_width // 2, 50 )
        textRect2.center = (display_width-100 , 50 )
        

        print(buffer)
        print(bufferstate)
        imgplace(Bground,0,0)  # Background
        
        pointer(black,x,y,20)
        drawer(places,colors)
        drawsquare(black,0,18,display_width,70)
        gameDisplay.blit(text, textRect)
        gameDisplay.blit(text2,textRect2)
        #bufferin=buffercheck(buffer,bufferstate)
        
        pygame.display.update()
        clock.tick(60)
        if checkok:
            print("Checks out!")


game_loop()
pygame.quit()
"""
Pontszámlásó         0
Körjelző            1/2
Indőmérő             0
Color change        1/2
Expand               0
Ways                 0



"""
quit()
