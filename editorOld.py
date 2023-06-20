import enum
import sys

import pygame

import build

pygame.init()

font  = pygame.font.Font("SpaceMono-Regular.ttf",15)

fsz = font.size("E")
uisz =(51,19)
sz = ((uisz[0]+1)*fsz[0],(uisz[1]+1)*fsz[1])
print(sz)
scr = pygame.display.set_mode(sz)

class mode(enum.IntEnum):
    text=1
    fg=2
    bg=3
    define = 4
    build=5
class UImode(enum.IntEnum):
    text=1
    fg=2
    bg=3


colors = [
    (240, 240, 240),
    (242, 178, 51),
    (229, 127, 216),
    (153, 178, 242),
    (222, 222, 108),
    (127, 204, 25),
    (242, 178, 204),
    (76, 76, 76),
    (153, 153, 153),
    (76, 153, 178),
    (178, 102, 229),
    (51, 102, 204),
    (127, 102, 76),
    (87, 166, 78),
    (204, 76, 76),
    (17, 17, 17)
]

content=[[" "for y in range(uisz[0])] for x in range(uisz[1])]
cbg = [[15 for y in range(uisz[0])] for x in range(uisz[1])]
cfg = [[0 for y in range(uisz[0])] for x in range(uisz[1])]
UI=["T","F","B","D","b"," ","#"]
UIRCT = [pygame.Rect(x*fsz[0],0,fsz[0],fsz[1]) for x,t in enumerate(UI)]
ufg = [5,1,2,14,13,15,5]

buttons =[]

curp = [0,0]
ccol = 5
md = mode.text
def posWrap(xy,mx,my=0):
    y,x=xy
    y+=mx
    x+=my
    if x>=uisz[1]:
        x=0
        y += 1
    if x<0:
        x=uisz[1]-1
        y -= 1
    if y>=uisz[0]:
        y=0
    return y,x
def setpos(y,x):
    global curp
    curp = (y,x)
def returnLn(xy):
    y,x=xy
    y=0
    x+=1
    
    return posWrap((y,x),0)
def fgbg(col,id):
    if md == id+1:
        return (255,255,255),col
    return col,(100,100,100)
def setCol(colN):
    global ccol
    ccol = colN
    ufg[6]=colN
setCol(0)
sel = pygame.Rect(0,0,1,1)
while True:
    if md == mode.build:
        build.build(content,cfg,cbg)
        md = 6
    scr.fill((0,0,0))
    for x,i in enumerate(UI):
        cpos = ((x)*fsz[0],(0)*fsz[1])
        fg,bg = fgbg(colors[ufg[x]],x)
        tx = font.render(i,True,fg,bg)
        scr.blit(tx,cpos)
    for y,r in enumerate(content):
        for x,i in enumerate(r):
            cpos = ((x)*fsz[0],(y+1)*fsz[1])
            if md == mode.define:
                if sel.collidepoint(x,y):
                    tx = font.render(i,True,colors[cfg[x][y]],(0,0,255))
                    scr.blit(tx,cpos)
                    continue
            tx = font.render(i,True,
                colors[
                    cfg[y][x]
                    ],
                colors[cbg[y][x]]
            )
            scr.blit(tx,cpos)
    
    cpos = (curp[0]*fsz[0],(curp[1]+1)*fsz[1])
    tx = font.render("_",True,colors[cfg[y][x]])
    scr.blit(tx,cpos)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            for I,i in enumerate(UIRCT):
                if i.collidepoint(e.pos):
                    md = I+1

        elif e.type == pygame.KEYDOWN:
            
            if md == mode.text:
                if e.key == pygame.K_BACKSPACE:
                    curp = posWrap(curp,-1)
                    content[curp[1]][curp[0]] = " "
                elif e.key == pygame.K_LEFT: curp = posWrap(curp,-1)
                elif e.key == pygame.K_RIGHT: curp = posWrap(curp,1)
                elif e.key == pygame.K_UP: curp = posWrap(curp,0,-1)
                elif e.key == pygame.K_DOWN: curp = posWrap(curp,0,1)
                elif e.key == pygame.K_RETURN: curp = returnLn(curp)
                else:
                    if e.unicode:
                        if ord(e.unicode):
                            content[curp[1]][curp[0]] = e.unicode
                            curp = posWrap(curp,1)
            elif md in (mode.fg,mode.bg):
                if e.key == pygame.K_LEFT: curp = posWrap(curp,-1)
                elif e.key == pygame.K_RIGHT: curp = posWrap(curp,1)
                elif e.key == pygame.K_UP: curp = posWrap(curp,0,-1)
                elif e.key == pygame.K_DOWN: curp = posWrap(curp,0,1)
                elif e.key == pygame.K_RETURN: curp = returnLn(curp)
                elif e.key == pygame.K_EQUALS: setCol((ccol+1)%16)
                elif e.key == pygame.K_MINUS: setCol((ccol-1)%16)
                else:
                    if md == mode.fg:
                        cfg[curp[1]][curp[0]] = ccol
                    else:
                        cbg[curp[1]][curp[0]] = ccol
                    curp = posWrap(curp,1)
            elif md == mode.define:
                if e.mod & pygame.KMOD_SHIFT:
                    if e.key == pygame.K_LEFT: sel.width-=1
                    elif e.key == pygame.K_RIGHT: sel.width+=1
                    elif e.key == pygame.K_UP: sel.height-=1
                    elif e.key == pygame.K_DOWN: sel.height+=1
                else:
                    if e.key == pygame.K_RETURN:
                        buttons.append(sel.copy())
                        sel = pygame.Rect(0,0,1,1)
                    elif e.key == pygame.K_LEFT: sel.x-=1
                    elif e.key == pygame.K_RIGHT: sel.x+=1
                    elif e.key == pygame.K_UP: sel.y-=1
                    elif e.key == pygame.K_DOWN: sel.y+=1


    pygame.display.flip()