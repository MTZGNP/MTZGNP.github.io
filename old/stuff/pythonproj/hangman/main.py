#!/usr/bin/env python
import pygame,sys
from pygame.locals import *
from random import choice as ranlist
pygame.init()
size=width , height = 500,500
screen=pygame.display.set_mode(size)
screen.fill((255,255,255))
alpha = list(map(chr, range(97, 123)))
font = pygame.font.Font('freesansbold.ttf', 32) 
heart=pygame.image.load("heart.png")
heart=pygame.transform.scale(heart,(50,50))
# create a text suface object, 
# on which text is drawn on it.  

def draw(see):
    screen.fill((255,255,255))
    
    for x in range(lives):
        screen.blit(heart,[10+(x*48),50])   
    char=font.render(" ".join(alpha[:13]), True,(0,0,255))
    screen.blit(char,[40,350])
    char=font.render(" ".join(alpha[13:25]), True,(0,0,255))
    screen.blit(char,[40,400])
    char=font.render(" ".join(see), True,(0,0,255))
    screen.blit(char,[40,200])
    pygame.display.flip()
raw ="""""".split()
###put the main dictionary here###
dic=['actor', 'airplane', 'airport', 'army', 'baseball', 'beef', 'birthday', 'boy', 'brush', 'bushes', 'butter', 'cast', 'cave', 'cent', 'cherries', 'cherry', 'cobweb', 'coil', 'cracker', 'dinner', 'eggnog', 'elbow', 'face', 'fireman', 'flavor', 'gate', 'glove', 'glue', 'goldfish', 'goose', 'grain', 'hair', 'haircut', 'hobbies', 'holiday', 'hot', 'jellyfish', 'ladybug', 'mailbox', 'number', 'oatmeal', 'pail', 'pancake', 'pear', 'pest', 'popcorn', 'queen', 'quicksand', 'quiet', 'quilt', 'rainstorm', 'scarecrow', 'scarf', 'stream', 'street', 'sugar', 'throne', 'toothpaste', 'twig', 'volleyball', 'wood', 'wrench']
##################################
dic+=raw
while True:
    alpha = list(map(chr, range(97, 123)))
    word=ranlist(dic)
    dic.remove(word)
    origword=[x for x in word]
    word=[x for x in word]
    lives=10
    see=["_"]*len(word)
    draw(see)
    while True:
        #exit cases
        if origword==see:
            pygame.time.wait(1000)
            screen.fill((0,255,25))
            
            char=font.render('you won',True,(0,0,0))
            screen.blit(char,[180,200])
            pygame.display.flip()
            pygame.time.wait(1000)
            break
        elif lives==0:
            pygame.time.wait(500)
            see=origword
            draw(see)
            pygame.time.wait(1000)
            screen.fill((255,0,25))
            char=font.render('you lose',True,(0,0,0))
            screen.blit(char,[180,200])
            pygame.display.flip()
            pygame.time.wait(1000)
            break
        choice=""
        event=pygame.event.wait()
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            choice = str(event.unicode)
            if choice in word :
                while choice in word:
                    see[word.index(choice)]=choice
                    word[word.index(choice)]=" "
                alpha[alpha.index(choice)]="-"    
            elif choice in alpha:
                lives-=1
                alpha[alpha.index(choice)]="-"
            draw(see)
        
