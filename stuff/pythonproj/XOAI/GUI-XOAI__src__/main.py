#!/usr/bin/env python
import pygame,sys
from pygame.locals import *
from random import choice
pygame.init()
f = None
logs={}
rects=[]
mult = 160
off = 90
font = pygame.font.Font('freesansbold.ttf', mult)
winfont = pygame.font.Font('freesansbold.ttf', 20)
for y,row in enumerate([["X","X","X"]]*3):
        y = (y*mult)+off
        for x,char in enumerate(row):
            if char in [str(x) for x in range(10)]:
                char = " "
            x = (x*mult)+off
            text = font.render(char,True,(0,0,0))
            rect = text.get_rect(center =(x,y))
            rects.append(rect)
board = pygame.transform.scale(pygame.image.load("package/board.jpg"),(500,500))
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
def win():
    wins = (
        grid[0],
        grid[1],
        grid[2],
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]],
        [grid[0][0], grid[1][0], grid[2][0]],
        [grid[0][1], grid[1][1], grid[2][1]],
        [grid[0][2], grid[1][2], grid[2][2]])
    if ["X", "X", "X"] in wins:
        return "X"
    elif ["O", "O", "O"] in wins:
        return "O"
    return 0
def update(log):
    for x in log.keys():
        if x in logs.keys():
            logs[x].append(log[x])
        else:
            logs[x] = [log[x]]
def remove(the_list, val):
    return [value for value in the_list if value != val]
def init():
    for y in range(3):
        for x in range(3):
            grid[y].append(str((y * 3) + x + 1))
    try:
        f = open("memory.txt", "r+")
    except:
        f = open("memory.txt", "x")
        f.close()
        f = open("memory.txt", "r+")
    f1 = f.readlines()
    for x in f1:
        sol = []
        for i in x[9:].strip("\n"):
            sol.append(int(i))
        logs[x[:9]] = sol
    f.close()
    oldlen = len(logs)
def waitformouse():
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            return 1
        if event.type == MOUSEBUTTONUP:
            for index,rect in enumerate(rects):
                if rect.collidepoint(pygame.mouse.get_pos()):
                    return index
def draw():
    screen.blit(board,(0,0))
    for y,row in enumerate(grid):
        y = (y*mult)+off
        for x,char in enumerate(row):
            if char in [str(x) for x in range(10)]:
                char = " "
            x = (x*mult)+off
            text = font.render(char,True,(0,0,0))
            rect = text.get_rect(center =(x,y))
            screen.blit(text,rect)
    pygame.display.flip()
play="y"
while play == "y":
    grid = [[], [], []]
    init()
    draw()
    pygame.event.clear()
    for turn in range(1, 10):
        draw()
        if win() != 0:
            draw()
            break
        if turn % 2 != 0:
            choice = waitformouse()
            x = int((choice) % 3)
            y = int((choice - x) / 3)
            while grid[y][x] not in [str(x) for x in range(10)]:
                choice = waitformouse()
                x = int((choice) % 3)
                y = int((choice - x) / 3)
            grid[y][x] = "X"
        else:
            gridlog = ""
            for x in grid:
                gridlog = gridlog + "".join(x)
            if gridlog in logs:
                choice = logs[gridlog][0]
                x = int((choice - 1) % 3)
                y = int((choice - 1 - x) / 3)
                grid[y][x] = "O"
            else:
                draw()
                pygame.time.wait(200)
                screen.fill((255,0,0))
                pygame.display.flip()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()
                
                break
    draw()
    if win()==0:
        pygame.time.wait(2000)
        screen.fill((255,255,255))
        char = winfont.render("it's a tie",True,(0,0,0))
        screen.blit(char,(200,200))
        pygame.display.flip()
        pygame.time.wait(3000)
    else:
        pygame.time.wait(2000)
        screen.fill((255,255,255))
        char = winfont.render("%s wins" % win(),True,(0,0,0))
        screen.blit(char,(200,200))
        pygame.display.flip()
        pygame.time.wait(3000)
