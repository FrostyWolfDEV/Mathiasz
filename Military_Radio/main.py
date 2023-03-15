import pygame
import random
import time
import threading   
pygame.init
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",100)
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
font = pygame.font.SysFont('timesnewroman',  30)
font2 =pygame.font.SysFont("font.ttf",30)
pygame.mixer.init()
difficulty=1    # Set Difficulty
def drawtoscreen(text,textRect):
    gameDisplay.blit(text,textRect)

def game_loop():
    letters=["Alpha","Beta","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliett","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu"]
    numbers=["One","Two","Three","Four","Five","Six","Seven","Eight","Niner","Zero"]
    say=""
    ndict={"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Niner","0":"Zero"}
    ldict={"A":"Alpha", "B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray","Y":"Yankee","Z":"Zulu"}
    game_exit=False
    user_text=""
    previus=""
    
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                game_exit = True
                engine.stop()
                print("Quit with event(quit)!")
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_p:    # Start readout
                    for i in range(random.randint(1+difficulty,4+difficulty+random.randint(0,2))):
                        coin=random.randint(0,1)
                        if coin==1:
                            say+=" "
                            say+=letters[random.randint(0,len(letters)-1)]
                        else:
                            say+=" "
                            say+=numbers[random.randint(0,len(numbers)-1)]
                    
                    engine.save_to_file(say,"say.mp3")
                    engine.runAndWait()
                    previus=say
                    say=""
                    saymp3=pygame.mixer.Sound(file="say.mp3")
                    pygame.mixer.Sound.play(saymp3,loops=0)
                if event.key==pygame.K_BACKSPACE:
                    try:
                        user_text=user_text[:-1]
                    except:
                        print("Backspace on empty string")
                elif event.key!=pygame.K_RETURN:
                    user_text+=event.unicode
                elif event.key==pygame.K_RETURN:
                    print(previus)
                    userlist=list(user_text)
                    for i in range(len(userlist)):
                        if not userlist[i].isnumeric():
                            userlist[i]=ldict.get(userlist[i])
                        else:
                            userlist[i]=ndict.get(userlist[i])
                    userlist = " ".join(userlist)
                    print(userlist)
                    print(previus)
                    if " "+userlist==previus:
                        user_text="Correct"
                    else:
                        user_text="Incorrect"
        gameDisplay.fill(black)
        text=font.render(user_text, True, red, None)
        title=font2.render("Militray Radio",True,green,None)
        text_rect=text.get_rect()
        title_rect=title.get_rect()
        title_rect.center=(display_width//2,100)
        text_rect.center=(display_width//2,display_height//2)
        drawtoscreen(text,text_rect)
        drawtoscreen(title,title_rect)
        


        pygame.display.update()
        clock.tick(60)
"""
 TODO:
    Numbers couse Error      (IP)





"""
game_loop()
pygame.quit()
quit()


