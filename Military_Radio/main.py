import pygame
from pygame.locals import *
import random
import time
import threading
import os   
pygame.init
import pyttsx3 # Text to Speech 
engine = pyttsx3.init()
engine.setProperty("rate",120)
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
darkgreen=(30, 117, 19)
font = pygame.font.SysFont('timesnewroman',  30)
activefile=0
generalID=""
targetAddres=""
font2 =pygame.font.Font("font.ttf",22)
font3= pygame.font.Font("font.ttf",40)
pygame.mixer.init()
difficulty=1    # Set Difficulty
def drawtoscreen(text,textRect):
    gameDisplay.blit(text,textRect)
def TextToScreen(font,text,color,x,y):
    textx=font.render(text,True,color,None)
    textRectx=textx.get_rect()
    textRectx.center=(x,y)
    drawtoscreen(textx,textRectx)
def ClickBox(x,y,width,height,border): # border=[True/False , color]
    #print(x,y,width,height,border)
    if border[0]==True:
        pygame.draw.aalines(gameDisplay,border[1],True,[(x,y),(x+width,y)])
        pygame.draw.aalines(gameDisplay,border[1],True,[(x,y),(x,y+height)])
        pygame.draw.aalines(gameDisplay,border[1],True,[(x,y+height),(x+width,y+height)])
        pygame.draw.aalines(gameDisplay,border[1],True,[(x+width,y+height),(x+width,y)])
        if pygame.mouse.get_pos()[0]>x and pygame.mouse.get_pos()[0]<x+width and pygame.mouse.get_pos()[1]>y and pygame.mouse.get_pos()[1]<y+height and pygame.mouse.get_pressed(num_buttons=3)[0]==True:
            return True
        else:
            return False
def Drawline(start,end,color):       
    pygame.draw.aalines(gameDisplay,color,True,[start,end])
def game_loop():
    letters=["Alpha","Beta","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliett","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu"]
    numbers=["One","Two","Three","Four","Five","Six","Seven","Eight","Niner","Zero"]
    say=""
    ndict={"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Niner","0":"Zero"}
    ldict={"A":"Alpha", "B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray","Y":"Yankee","Z":"Zulu"}
    game_exit=False
    user_text=""
    previus=""
    generalID=""
    targetAddres=""
    massage=""
    UIDSAY=""
    TRGSAY=""
    response=""
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                game_exit = True
                engine.stop()
                print("Quit with event(quit)!")
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_RSHIFT:    #  Start readout
                    for i in range(4):
                        coin=random.randint(0,1)
                        if coin==1:
                            UIDSAY+=" "
                            UIDSAY+=letters[random.randint(0,len(letters)-1)]
                        else:
                            UIDSAY+=" "
                            UIDSAY+=numbers[random.randint(0,len(numbers)-1)]
                    for i in range(4):
                        coin=random.randint(0,1)
                        if coin==1:
                            TRGSAY+=" "
                            TRGSAY+=letters[random.randint(0,len(letters)-1)]
                        else:
                            TRGSAY+=" "
                            TRGSAY+=numbers[random.randint(0,len(numbers)-1)] 
                    for i in range(random.randint(1+difficulty,4+difficulty+random.randint(0,2))):
                        coin=random.randint(0,1)
                        if coin==1:
                            say+=" "
                            say+=letters[random.randint(0,len(letters)-1)]
                        else:
                            say+=" "
                            say+=numbers[random.randint(0,len(numbers)-1)]
                    user_text=""
                    previus=say
                    previusTRG=TRGSAY
                    previusUID=UIDSAY
                    TRGSAY= "Target: " + TRGSAY
                    UIDSAY=" Universal I D: " + UIDSAY
                    say="Message: "+ say
                    unifiedsay=UIDSAY+": "+ TRGSAY+": "+ say
                    print(unifiedsay)
                    engine.save_to_file(unifiedsay,"say.mp3")
                    engine.runAndWait()
                    
                    say=""
                    saymp3=pygame.mixer.Sound(file="say.mp3")
                    
                    
                    
                    pygame.mixer.Sound.play(saymp3,loops=0)
                if event.key==pygame.K_RCTRL:   # Debug event
                    user_text= pygame.mouse.get_pressed(num_buttons=3)[0]
                if event.key==pygame.K_BACKSPACE:
                    try:
                        if activefile==0:
                            generalID=generalID[:-1]
                        elif activefile==1:
                            targetAddres=targetAddres[:-1]
                        elif activefile==2:
                            massage=massage[:-1]
                        elif activefile==3:
                            response=response[:-1]
                    except:
                        print("Backspace on empty string")
                elif event.key!=pygame.K_RETURN:
                    try:
                        if activefile==0:
                            generalID+=event.unicode
                        elif activefile==1:
                            targetAddres+=event.unicode
                        elif activefile==2:
                            massage+=event.unicode
                        elif activefile==3:
                            response+=event.unicode
                    except:
                        print("Non unicode character")
                elif event.key==pygame.K_RETURN:
                    
                    userlist=list(massage)
                    for i in range(len(userlist)):
                        if not userlist[i].isnumeric():
                            userlist[i]=ldict.get(userlist[i])
                        else:
                            userlist[i]=ndict.get(userlist[i])
                    userlist = " ".join(userlist)
                    print(userlist)
                    print(previus)
                    if " "+userlist==previus:
                        user_text="Massage Authenticated Correctly!"
                    else:
                        user_text="Massage Authenticated Incorrectly!"
        gameDisplay.fill(black)
        text=font3.render(str(user_text), True, red, None)
        title=font2.render("Militray Radio",True,darkgreen,None)
        text_rect=text.get_rect()
        title_rect=title.get_rect()
        title_rect.center=(display_width//2,60)
        text_rect.center=(display_width//2,display_height//2-200)
        drawtoscreen(text,text_rect)
        drawtoscreen(title,title_rect)
        TextToScreen(font2,"Universal ID",darkgreen,200,display_height//2-40)
        TextToScreen(font2,"Target Address",darkgreen,500,display_height//2-40)
        TextToScreen(font2,"Message",darkgreen,950,display_height//2-40)
        TextToScreen(font2,"This software if for official military use only! Any personal use of this software is considered a federal crime!",darkgreen,display_width//2,display_height-30)
        Click=ClickBox(100,display_height//2,200,50,[True,red])
        targetClick=ClickBox(400,display_height//2,200,50,[True,red])
        massageClick=ClickBox(700,display_height//2,500,50,[True,red])
        responseClick=ClickBox(display_width//2-250,display_height//2+200,500,50,[True,red])
        
        if Click: # Click detectors
            activefile=0
        TextToScreen(font2,generalID,darkgreen,200,display_height//2+25)
        if targetClick:
            activefile=1
        if massageClick:
            activefile=2
        if responseClick:
            activefile=3
        TextToScreen(font2,"Response",darkgreen,display_width//2,display_height//2+150)
        TextToScreen(font2,response,darkgreen,display_width//2,display_height//2+225)

        TextToScreen(font2,massage,darkgreen,950,display_height//2+25)
        TextToScreen(font2,targetAddres,darkgreen,500,display_height//2+25)
        Drawline([0,display_height-50],[display_width,display_height-50],darkgreen)
        Drawline([display_width-350,0],[display_width-350,display_height-50],darkgreen)
        TextToScreen(font2,"News:",darkgreen,display_width-200,50)
        pygame.display.update()
        clock.tick(60)
"""
 TODO:
    Numbers couse Error             (Done)
    Better Looking Display          (IP)
    GITHUB quicksave branch         (Working)
    Command to reply back with      (IP)



"""
game_loop()
pygame.quit()
quit()


