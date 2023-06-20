import enum
import sys

import pygame
import pygame_menu

import build
import elements

pygame.init()

font  = pygame.font.Font("SpaceMono-Regular.ttf",15)

fsz = font.size("E")
elements.fsz = fsz
elements.font = font
uisz =(51,19)
sz = ((uisz[0])*fsz[0],(uisz[1]+1)*fsz[1])
print(sz)
scr = pygame.display.set_mode(sz)

menu = pygame_menu.Menu('Text', 400, 300,
                       theme=pygame_menu.themes.THEME_DARK)
menu.disable()



class mode(enum.IntEnum):
    text=1
    fg=2
    bg=3
    define = 4
    build=5
    code=6
class UImode(enum.IntEnum):
    text=1
    fg=2
    bg=3


colors = elements.colors

content:list[elements.element]=[]


md = mode.define
sel = pygame.Rect(0,0,1,1)
SEL = pygame.Rect(0,0,fsz[0],fsz[1])
def chngSEL():
    global SEL
    SEL.x,SEL.y = sel.x*fsz[0],sel.y*fsz[1]
    SEL.width,SEL.height = sel.width*fsz[0],sel.height*fsz[1]
clock = pygame.time.Clock()
btmBar = pygame.Rect(0,sz[1]-fsz[1],sz[0],fsz[1])
elements.btmBar =sz[1]-fsz[1]
tools = [elements.tool('»',mode.build,0),elements.tool("±",mode.define,1),elements.tool("¶",mode.text,2),elements.tool("‡",mode.code,3)]
selelemtype = 0
selElem = -1
def conf(ln):
    def c(value):
        print(value)
        content[selElem].editText(value,ln)
        #menu.disable()
    return c
def done():
    menu.disable()

while True:
    clock.tick(30)
    pygame.display.set_caption(f"fps:{str(clock.get_fps())}")
    if md == mode.build:
        pass
        #build.build(content,cfg,cbg)
        #md = 6
    scr.fill((17,17,17))
    
    if md == mode.define:
        scr.fill((0,0,255),SEL)
        

    for i in content:
        i.draw(scr,md==mode.define)
    if selElem >-1:
        content[selElem].draw(scr,True)

    scr.fill((0,0,0),btmBar)
    for i in tools:
        i.draw(scr,md)
    
    evnts =pygame.event.get()
    if menu.is_enabled():
        menu.draw(scr)
        menu.update(evnts)
    else:
        for e in evnts:
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                for t in tools:
                    if t.rect.collidepoint(e.pos):
                        md = t.id
                if md == mode.text:
                    for I,i in enumerate(content):
                        if i.rectE.collidepoint(e.pos):
                            tools[2].col = colors[i.color]
                            selElem = I
                            break
                        selElem = -1
                        tools[2].col = colors[0]

            elif e.type == pygame.KEYDOWN:
                
                if md == mode.text:
                    if e.key == pygame.K_BACKSPACE:
                        pass
                    elif e.key == pygame.K_LEFT:pass
                    elif e.key == pygame.K_RIGHT:pass
                    elif e.key == pygame.K_UP:pass
                    elif e.key == pygame.K_DOWN:pass
                    elif e.key == pygame.K_RETURN:
                        menu = pygame_menu.Menu(f'{str(selElem)}', 400, 300,theme=pygame_menu.themes.THEME_DARK)
                        for i in range(1,content[selElem].rect.height-1):

                            menu.add.text_input(f'Line {str(i)}:', default='',onreturn=conf(i))
                        menu.add.button('Done', done)
                        menu.enable()
                    else:
                        if e.unicode:
                            if ord(e.unicode):
                                pass
                elif md in (mode.fg,mode.bg):
                    if e.key == pygame.K_LEFT:pass
                    elif e.key == pygame.K_RIGHT:pass
                    elif e.key == pygame.K_UP:pass
                    elif e.key == pygame.K_DOWN:pass
                    elif e.key == pygame.K_RETURN:pass
                    elif e.key == pygame.K_EQUALS:pass
                    elif e.key == pygame.K_MINUS:pass
                    else:
                        if md == mode.fg:
                            pass
                        else:
                            pass
                        
                elif md == mode.define:
                    if e.mod & pygame.KMOD_SHIFT:
                        
                        if e.key == pygame.K_LEFT: sel.width-=1
                        elif e.key == pygame.K_RIGHT: sel.width+=1
                        elif e.key == pygame.K_UP: sel.height-=1
                        elif e.key == pygame.K_DOWN: sel.height+=1
                        chngSEL()
                    else:
                        if e.key == pygame.K_RETURN:
                            content.append(elements.elems[selelemtype](sel.copy()))
                            sel = pygame.Rect(0,0,1,1)
                        elif e.key == pygame.K_LEFT: sel.x-=1
                        elif e.key == pygame.K_RIGHT: sel.x+=1
                        elif e.key == pygame.K_UP: sel.y-=1
                        elif e.key == pygame.K_DOWN: sel.y+=1
                        elif e.key == pygame.K_MINUS:
                            selelemtype = (selelemtype-1)%len(elements.elems)
                            tools[1].col = colors[elements.elems[selelemtype].bg]
                        elif e.key == pygame.K_EQUALS:
                            selelemtype = (selelemtype+1)%len(elements.elems)
                            tools[1].col = colors[elements.elems[selelemtype].bg]
                        chngSEL()


    pygame.display.flip()