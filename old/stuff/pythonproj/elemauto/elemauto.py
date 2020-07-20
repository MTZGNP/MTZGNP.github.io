import sys, pygame
from time import sleep
from random import choice,randint
pygame.init()
screen,fl = None , None
def intinp(message):
    while True:
        try:
            return int(input(message))
            break
        except:
            print("ONLY DATA OF TYPE INTEGER IS ALLOWED")
#user variables
def elemauto(tick=True,cells=True,ruleset=True,msize=True,render=True,gens=True):
    global screen , fl
    if tick==True :
        try:
            int(tick)
        except:
            tick= int(intinp("Enter tick# (ms): "))
    if cells == True:    
        mode=input("    ------ \n enter mode: \n    |=> manual : manually type a board \n    |=> #: make a random board of # size \n=>")
        cells=[]
        if mode=="manual":
            cells=[int(x) for x in input("------\nenter :\n")]
        else:
            cells = [choice([0,1]) for x in range(intinp("__________\nenter size of randomly generated board:\n"))]    
    if msize == True:
        msize = intinp("------\nenter size of module:")
    if gens  == True:
        gens=intinp("------\nenter# of gens :")
    if ruleset == True:    
        random={}
        rulesets={
            "101":{
            "000":0,
            "001":0,
            "010":0,
            "011":0,
            "100":1,
            "101":1,
            "110":1,
            "111":0
            },
            "105":{
            "000":1,
            "001":0,
            "010":0,
            "011":1,
            "100":0,
            "101":1,
            "110":1,
            "111":0
            
                },
            "154":{
                "000":0,
                "001":1,
                "010":0,
                "011":1,
                "100":1,
                "101":0,
                "110":0,
                "111":1
                },
            "184":{
                "000":0,
                "001":0,
                "010":0,
                "011":1,
                "100":1,
                "101":1,
                "110":0,
                "111":1
                },
            "30":{
                "000":0,
                "001":1,
                "010":1,
                "011":1,
                "100":1,
                "101":0,
                "110":0,
                "111":0
                }
        }
        for x in rulesets["101"].keys():
            random[x]=choice([1,0])
        rulesets["random"]=random
        print("______\n\nChoose ruleset:")
        for x in rulesets.keys():
            print("    =>",x)
        ruleset=rulesets[input("=>")]
    if render==True:
        try:
            int(render)
        except:    
            render=intinp("____\nenter render mode \n    |=>1:continous \n    |=>0:singular \n=>")
    print("elemauto(tick=%d,cells=%s,ruleset=%s,msize=%d,render=%d,gens=%d)" % (tick,cells,ruleset,msize,render,gens))         
    offset = msize
    fl = input("enter file name")
#pygame variables

    def init(w,h):
        size = width, height = w,h
        black = (0, 0, 0)
        white = (255,255,255)
        colors={1:black,0:white}
        screen = pygame.display.set_mode(size)
        rects = []
        running=1
        screen.fill((255,255,0))
        return size,colors,screen,rects,running



    def draw(gen):
        if not render:
            screen.fill((255,255,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        rects = []    
        for x in range(0,len(cells)):
            CurrRect=pygame.Rect(20,20,msize,msize)
            CurrRect.center = ((x*msize)+offset+(msize/2),offset+(msize/2)+(render*(gen*msize)))
            CurrRect=pygame.draw.rect(screen,colors[cells[x]],CurrRect)
        pygame.display.flip()

    if render:
        size,colors,screen,rects,running = init((len(cells)*msize)+offset*2,(gens*msize)+40)
    else:
        size,colors,screen,rects,running = init((len(cells)*msize)+offset*2,msize+offset*2)
    for y in range(gens):
        draw(y)
        pygame.time.delay(tick)
        temp=cells[:]

        temp[-1]=ruleset["".join([str(x) for x in cells[-2:]+[cells[0]]])]
        temp[0]=ruleset["".join([str(x) for x in [cells[-1]]+cells[0:2]])]
        for x in range(1,len(cells)-1):
            temp[x]=ruleset["".join([str(x) for x in cells[x-1:x+2]])]
        cells=temp[:]
    
exec(input("enter quick code or type \"elemauto()\" to go to selection:"))
pygame.time.wait(5000)
pygame.image.save(screen,"elem-auto-%s.png" % fl)
#try
#elemauto(tick=1,cells=[1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],ruleset={'000': 1, '001': 0, '010': 0, '011': 1, '100': 0, '101': 1, '110': 0, '111': 1},msize=2,render=1,gens=500)
#elemauto(tick=1,msize=1,render=1,gens=1000)
#all black 1000 cells
#elemauto(tick=1,msize=1,render=1,gens=1000,cells=[1]*1000)
#all white 1000 cells
#elemauto(tick=1,msize=1,render=1,gens=1000,cells=[0]*1000)
#all white with middle black
#elemauto(tick=1,msize=1,render=1,gens=1000,cells=([0]*500)+[1]+([0]*500))
#all black with middle white
#elemauto(tick=1,msize=1,render=1,gens=1000,cells=([1]*500)+[0]+([1]*500))
#random cells
#elemauto(tick=1,msize=1,render=1,gens=1000)
#random cells and gens
#elemauto(tick=1,msize=1,render=1)
#pattern gen for rule-30
#elemauto(tick=1,msize=1,render=1,gens=1000,cells=[0,0,0,0,1,0,0,0,1,1,1,0,0,0]*50)
