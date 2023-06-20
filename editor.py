import enum
import sys

import pygame
import pygame_menu

import build
import elements

pygame.init()

mytheme = pygame_menu.themes.THEME_DARK.copy()
mytheme.widget_font_size = 15
mytheme.title_close_button = True
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
    edit=1
    define = 2
    build=3
    code=4
class UImode(enum.IntEnum):
    text=1
    fg=2
    bg=3


colors = elements.colors

content:list[elements.element]=[]
items = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5, "6":6,"7":7,"8":8,"9":9, "a":10,"b":11,"c":12,"d":13,"e":14,"f":15}

md = mode.define
sel = pygame.Rect(0,0,1,1)
SEL = pygame.Rect(0,0,fsz[0],fsz[1])
def chngSEL():
    global SEL
    SEL.x,SEL.y = sel.x*fsz[0],sel.y*fsz[1]
    SEL.width,SEL.height = sel.width*fsz[0],sel.height*fsz[1]
def colorBG(selected_value, color, **kwargs):
    content[selElem].color = color
clock = pygame.time.Clock()
btmBar = pygame.Rect(0,sz[1]-fsz[1],sz[0],fsz[1])
elements.btmBar =sz[1]-fsz[1]
tools = [elements.tool('»',mode.build,0),elements.tool("±",mode.define,1),elements.tool("¶",mode.edit,2),elements.tool("‡",mode.code,3)]
selelemtype = 0
selElem = -1
def conf(ln):
    def c(value):
        #print(value)
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
                if md == mode.edit:
                    for I,i in enumerate(content):
                        if i.rectE.collidepoint(e.pos):
                            tools[2].col = colors[type(i).bg]
                            selElem = I
                            break
                        selElem = -1
                        tools[2].col = colors[0]

            elif e.type == pygame.KEYDOWN:
                
                if md == mode.edit:
                    if e.key == pygame.K_BACKSPACE:
                        pass
                    elif e.key == pygame.K_LEFT:pass
                    elif e.key == pygame.K_RIGHT:pass
                    elif e.key == pygame.K_UP:pass
                    elif e.key == pygame.K_DOWN:pass
                    elif e.key == pygame.K_RETURN:
                        menu = pygame_menu.Menu(f'{str(selElem)}', 400, 300,theme=mytheme,)
                        menu.add.selector(
                            title='Background:',
                            items=list(items.items()),
                            onreturn=colorBG, 
                            onchange=colorBG
                        )
                        if content[selElem].rect.height <=2:
                            for i in range(content[selElem].rect.height):
                             menu.add.text_input(f'Line {str(i)}:', default='',onreturn=conf(i),onchange=conf(i))

                        else:
                            for i in range(1,content[selElem].rect.height-1):
    
                                menu.add.text_input(f'Line {str(i)}:', default='',onreturn=conf(i),onchange=conf(i))
                        
                        menu.add.button('Done', done)
                        menu.enable()
                    else:
                        if e.unicode:
                            if ord(e.unicode):
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