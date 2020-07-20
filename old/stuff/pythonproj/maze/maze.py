import pygame,sys
from pygame.locals import *
from math import ceil
pygame.init()
BG = 255,255,255
video_infos = pygame.display.Info()
height, width =video_infos.current_h - 20 , video_infos.current_w-30
maze=pygame.image.load("maze.png")
if maze.get_size()[0]<width:
    width = ceil((maze.get_size()[0]/maze.get_size()[1])*height)
screen = pygame.display.set_mode((width, height),RESIZABLE)
#!--maze--#
maze = pygame.transform.scale(maze,(width,height))
maze_mask=pygame.mask.from_surface(maze)
maze_rect=maze.get_rect()
win_rect = pygame.draw.rect(screen,(0,255,0),(50,50,width-100,height-100))
win_size = 50
win_x = -40
win_y = -40
bound_x = width-win_size + win_x
bound_y = height - win_size +win_y

#!--ball--#
ball=pygame.transform.scale(pygame.image.load("sprite.png").convert_alpha(),(round(width/25),round(width/25)))
ball_mask=pygame.mask.from_surface(ball)
ball_rect=ball.get_rect()
vx , vy = 0,0
accel , deaccel = 5,4
#=>ball physics--#
vx,vy = 0,0
bounce=0.1
x , y =30,0
#!--main loop--#
FPS=30
tick=round(1000/FPS)
while True:
    pygame.time.wait(tick)
    #!--shutoff detection--#
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #!--ball control--#
    keys=pygame.key.get_pressed()
    #!--win detection--#
    
    if x > bound_x and y > bound_y:
        pygame.time.wait(1000)
        screen.fill((0,255,0))
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render('you win', True, (0,0,0) ,(0,255,0)) 
        textRect = text.get_rect()  
        textRect.center = (width/ 2, height/ 2)
        screen.blit(text,textRect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
        #!--collision detection--#
    elif maze_mask.overlap(ball_mask,((ceil(x+vx),ceil(y+vy)))) != None :
        x-=vx
        y-=vy
    else:
        if keys[K_LEFT]:
            vx-=accel
        if keys[K_RIGHT]:
            vx+=accel
        if keys[K_UP]:
            vy-=accel
        if keys[K_DOWN]:
            vy+=accel

    
        #!--friction--#
    if vx!=0:
        vx+= (0-vx)/3
    if vy!=0:
        vy+= (0-vy)/3
    x+=vx
    y+=vy
    
    #!--draw--#
    screen.fill(BG)
    pygame.draw.rect(screen,(0,255,0),(bound_x,bound_y,win_size,win_size))
    screen.blit(ball,(x,y))
    screen.blit(maze,(0,0))
    pygame.display.flip()

    
    

