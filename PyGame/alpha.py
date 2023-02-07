import pygame
import random
from PIL import Image
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Test')
clock = pygame.time.Clock()
img = Image.open("chr_p.png")
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
rocket=pygame.image.load("chr_p.png")
x_change=0
y_change=0
car_width=img.width
car_height=img.height

print(car_width)
print(car_height)


poinst=0
scored=0

collicion_x=car_width/2
collicion_y=car_height/2
def car(x,y):
    gameDisplay.blit(rocket, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def around(x,thingx,prec):
    if abs(x-thingx)<prec:
        return True
    else:
        return False




def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    lastevents=[0,0,0,0]
    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = random.randrange(0,display_height)
    thing_speed = 0
    thing_width = 25
    thing_height = 25
    thing_collocion_x=thing_width/2
    thing_collocion_y=thing_height/2
    points=0


    gameExit = False
    


    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                print("Quit with event(quit)!")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lastevents[0]=1
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    lastevents[1]=1
                    x_change = 20
                elif event.key == pygame.K_UP:
                    lastevents[2]=1
                    y_change = -20
                elif event.key == pygame.K_DOWN:
                    lastevents[3]=1
                    y_change = 20

                if event.key == pygame.K_RETURN:
                    thing_startx = random.randrange(0, display_width)
                    thing_starty = random.randrange(0,display_height)
            if event.type == pygame.KEYUP:
                

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if event.key ==pygame.K_LEFT:
                        lastevents[0]=0
                    elif event.key ==pygame.K_RIGHT:
                        lastevents[1]=0
                    x_change = 0
                elif event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                    if event.key ==pygame.K_UP:
                        lastevents[2]=0
                    elif event.key ==pygame.K_DOWN:
                        lastevents[3]=0
                    y_change = 0
        print(lastevents)
        if x > display_width - car_width or x < 0:
            if x > display_width - car_width and lastevents[1]==1:
                x_change=0
                print("Right interrupt")
            elif x < 0 and lastevents[0]==1:
                x_change=0
        if y > display_height - car_height or y < 0:
            if y > display_height - car_height and lastevents[3]==1:
                y_change=0
            elif y < 0 and lastevents[2]==1:
                y_change=0

        x += x_change
        y += y_change
        if around(x+collicion_x,thing_startx+thing_collocion_x,thing_width+car_width/2) and around(y+collicion_y,thing_collocion_y+thing_starty,thing_height):
            if scored!=1:
                points+=1
            print("Collision!")
            thing_startx = random.randrange(0, display_width)
            thing_starty = random.randrange(0,display_height)
        else:
            print(x,thing_startx,y,thing_starty,around(x,thing_startx,10),around(y,thing_starty,10),points,sep=" ")
            scored=0
            

        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        car(x,y)
        things(x, y, 5, 5, red) # left_top
        things(x+car_width,y+car_height,5,5,red) #right_bottom
        things(x,y+car_height,5,5,red) # left_bottom
        things(x+car_width,y,5,5,red)
        things(x+collicion_x, y+collicion_y, 10, 10, red)
        things(thing_collocion_x+thing_startx,thing_collocion_y+thing_starty,5,5,red)

        
        pygame.display.update()
        clock.tick(15)

game_loop()
pygame.quit()
quit()