import pygame,sys,enum,build,elements
pygame.init()

font  = pygame.font.Font("SpaceMono-Regular.ttf",15)

fsz = font.size("E")
elements.fsz = fsz
uisz =(51,19)
sz = ((uisz[0])*fsz[0],(uisz[1])*fsz[1])
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

content:list[elements.element]=[]

md = mode.define
sel = pygame.Rect(0,0,1,1)
SEL = pygame.Rect(0,0,fsz[0],fsz[1])
def chngSEL():
    global SEL
    SEL.x,SEL.y = sel.x*fsz[0],sel.y*fsz[1]
    SEL.width,SEL.height = sel.width*fsz[0],sel.height*fsz[1]
clock = pygame.time.Clock()
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
        scr.fill(colors[i.color],i.rectE)
        pygame.draw.rect(scr,(255,255,255),i.rectE,2)

    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            pass

        elif e.type == pygame.KEYDOWN:
            
            if md == mode.text:
                if e.key == pygame.K_BACKSPACE:
                    pass
                elif e.key == pygame.K_LEFT:pass
                elif e.key == pygame.K_RIGHT:pass
                elif e.key == pygame.K_UP:pass
                elif e.key == pygame.K_DOWN:pass
                elif e.key == pygame.K_RETURN:pass
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
                        content.append(elements.element(sel.copy()))
                        sel = pygame.Rect(0,0,1,1)
                    elif e.key == pygame.K_LEFT: sel.x-=1
                    elif e.key == pygame.K_RIGHT: sel.x+=1
                    elif e.key == pygame.K_UP: sel.y-=1
                    elif e.key == pygame.K_DOWN: sel.y+=1
                    chngSEL()


    pygame.display.flip()