try:
    import pygame,sys
    from pygame.locals import *
    from random import randint
    from math import sqrt
    pygame.init()
    screen = pygame.display.set_mode((0,0),FULLSCREEN)
    surf = pygame.display.get_surface() #get the surface of the current active display
    w,h = size = surf.get_width(), surf.get_height()
    image = pygame.image.load("image.png")
    imgsize=20
    image = pygame.transform.scale(image,(imgsize,imgsize))
    screen.fill((255,255,255))
    x=randint(imgsize,w-imgsize)
    y=randint(imgsize,h-imgsize)
    rect = pygame.draw.rect(screen,(255,255,255),(x,y,imgsize,imgsize))
    cx , cy = rect.centerx , rect.centery
    maxw=max([cx,w-cx])
    maxh=max([cy,h-cy])
    maxd=sqrt((maxw**2)+(maxh**2))
    #screen.blit(image,(x,y))
    run=True
    tick=100
    while run:
        pygame.time.wait(tick)
        event= pygame.event.wait()
        if event.type ==QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(image,(x,y))
            pygame.display.flip()
            pygame.time.wait(2000)
            screen.fill((0,255,0))
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('you win', True,(0,0,0))
            textRect = text.get_rect()
            textRect.center = (w/2,h/2)
            screen.blit(text,textRect)
            pygame.display.flip()
            x=randint(imgsize,w-imgsize)
            y=randint(imgsize,h-imgsize)
            rect = pygame.draw.rect(screen,(255,255,255),(x,y,100,100))
            cx , cy = rect.centerx , rect.centery
            pygame.time.wait(2000)
        dx=abs(cx-pygame.mouse.get_pos()[0])
        dy=abs(cy-pygame.mouse.get_pos()[1])
        d=sqrt((dx**2)+(dy**2))
        #!----draw----#
        screen.fill((255,255,255))
        if d > maxd:
            maxd=d
        color=((255*d)/maxd,255-((255*d)/maxd),0)
        pointer = pygame.draw.rect(screen,color,(0,0,50,50))
        pygame.display.flip()
except:
#!-----exit------#
    pygame.quit()
    sys.exit()
