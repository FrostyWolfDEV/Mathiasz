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

            #colorinfo2= ast.literal_eval(colorinfo)  # CRASH!!!
            #cords2= ast.literal_eval(cords)          # CRASH!!!
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
def getquestion(usedszam):  #                            ##Question chooser##
    kerdesek=open("questions.txt","r",encoding="UTF-8" )
    for i in range(usedszam):
        linex=kerdesek.readline()
    if usedszam==0:
        usedszam+=1
        linex=kerdesek.readline()
    answerslist=[]
    if "<Q>" in linex:
        linex=list(linex)
        print(linex)
        for i in range(3):
            linex.pop(0)
        
        answers=linex[0]
        linex.pop(0)
        for i in range(int(answers)):
            answerslist.append(kerdesek.readline())
            usedszam+=1
    usedszam+=1 # Correction for distortion
    returnlist=["".join(linex)[:-1],usedszam,answerslist]
    return returnlist
             
def getcorrectanswer(answers):
    for i in range(len(answers)-1):
        if list(answers[i])[0]=="R":
            goodanswer=i
    return goodanswer

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
    flipflop=True
    places=[]
    colors=[]
    citynames=[]
    lastturn=0
    index=0
    teamturn=0
    colorcounter=0
    colorset=[red,green,blue,white]
    font = pygame.font.SysFont('timesnewroman',  30)
    usedszam=0
    questionreturn=getquestion(usedszam)
    question=questionreturn[0]
    usedszam=questionreturn[1]
    answers=questionreturn[2]
    buffer=""
    bufferstate=""
    correctanswer=0
    spread=loadfromlong()
    colors=spread[1]
    places=spread[0]
    turn=0
    checkok=False
    answerswitch=1
    goodanswer=getcorrectanswer(answers) 
    print(colors)
    print(places)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit + save dots to short term save
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
                    
                    if answerswitch==0:
                        questionreturn=getquestion(usedszam)
                        usedszam=questionreturn[1]
                        question=questionreturn[0]
                        answers=questionreturn[2]
                        turn+=1
                        answerswitch=1
                    elif answerswitch==1:
                        answerswitch=0
                        goodanswer=getcorrectanswer(answers) 
                    


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
        #                  Text setup
        text = font.render(question, True, red, None)
        text2= font.render(str(turn)+"/30",True,red,None)
        #                   Answers
        if len(answers)>0 :
            if answerswitch==1 or goodanswer==0:
                answ1= font.render(answers[0][1:-1],True,red,None)
            else:
                answ1= font.render("",True,red,None)
        else:
            answ1= font.render("",True,red,None)
        if len(answers)>1:
            if answerswitch==1 or goodanswer==1:
                answ2= font.render(answers[1][1:-1],True,red,None)
            else:
                answ2= font.render("",True,red,None)
        else:
            answ2= font.render("",True,red,None)
        if len(answers)>2:
            if answerswitch==1 or goodanswer==2:
                answ3= font.render(answers[2][1:-1],True,red,None)
            else:
                answ3= font.render("",True,red,None)
        else:
            answ3= font.render("",True,red,None)
        if len(answers)>3:
            if answerswitch==1 or goodanswer==3:
                answ4= font.render(answers[3][1:-1],True,red,None)
            else:
                answ4= font.render("",True,red,None)
        else:
            answ4= font.render("",True,red,None)
        #                  Rect Setup
        textRect = text.get_rect()
        textRect2=text2.get_rect()
        answ1Rect=answ1.get_rect()
        answ2Rect=answ2.get_rect()
        answ3Rect=answ3.get_rect()
        answ4Rect=answ4.get_rect()
        textRect.center = (display_width // 2, 50 )
        textRect2.center = (display_width-100 , 50 )
        answ1Rect.center = (display_width-300, display_height-250)
        answ2Rect.center = (display_width-300, display_height-180)
        answ3Rect.center = (display_width-300, display_height-120)
        answ4Rect.center = (display_width-300, display_height-50)


        
            
            
        #print(places)
        #print(citynames)
        #gameDisplay.blit(citynames[1],citynames[0])
        #print(citynames[1],citynames[0])
                

        print(buffer)
        print(bufferstate)
        imgplace(Bground,0,0)  # Background        If you put anything onto the screen, do it from UNDER here(!!!!) (idiot)
        
        pointer(black,x,y,20)
        for listas in places:
        
            cityx=listas[0]
            cityy=listas[1]-30
            
            cityname=font.render("Test",True,black,None)
            cityRect= cityname.get_rect()
            cityRect.center = (cityx,cityy)
            print(cityx,cityy,cityname,cityRect) 
            gameDisplay.blit(cityname, cityRect)
        
            
        drawer(places,colors)
        drawsquare(black,0,18,display_width,70)
        drawsquare(black,display_width-500,display_height-300,500,300)
        if bufferstate!="":
            pointer(red,display_width-200,50,5)
        if lastturn!=turn:
            lastturn=turn
            if teamturn<3:
                teamturn+=1
            else:
                teamturn=0
        pointer(colorset[teamturn],display_width-250,50,5)
        gameDisplay.blit(text, textRect)
        gameDisplay.blit(text2,textRect2)
        gameDisplay.blit(answ1,answ1Rect)
        gameDisplay.blit(answ2,answ2Rect)
        gameDisplay.blit(answ3,answ3Rect)
        gameDisplay.blit(answ4,answ4Rect)
        #bufferin=buffercheck(buffer,bufferstate)
        
        pygame.display.update()
        clock.tick(60)
        if checkok:
            print("Checks out!")


game_loop()
pygame.quit()
"""
Pontszámlásó(?)      0
Körjelző            Done
Indőmérő             0
Color change        1/2
Expand               0
Ways                 0
Answers             Done

Városok: 
Balatonfenyves 
Fonyód
Balatonboglár
Balatonszárszó
Zamárdi 
Siófok

Balatonvilágos
Balatonalmádi
Balatonfüred 
Tihany
Zánka
Szigliget 
Kesztely

"""
quit()
