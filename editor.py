import pygame,sys,enum
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

content=[[" "for y in range(uisz[1])] for x in range(uisz[0])]
cbg = [[15 for y in range(uisz[1])] for x in range(uisz[0])]
cfg = [[0 for y in range(uisz[1])] for x in range(uisz[0])]
UI=["T","F","B"," ","#"]
ufg = [5,1,2,15,5]

curp = [0,0]
ccol = 5
md = mode.text
def posWrap(xy,mx,my=0):
    x,y=xy
    x+=mx
    y+=my
    if x>=uisz[0]:
        x=0
        y += 1
    if x<0:
        x=uisz[0]-1
        y -= 1
    if y>=uisz[1]:
        y=0
    return x,y
def returnLn(xy):
    x,y=xy
    x=0
    y+=1
    
    return posWrap((x,y),0)
def fgbg(col,id):
    if md == id+1:
        return (255,255,255),col
    return col,(100,100,100)
def setCol(colN):
    ccol = colN
    ufg[4]=colN
setCol(0)
while True:
    scr.fill((0,0,0))
    for x,i in enumerate(UI):
        cpos = ((x)*fsz[0],(0)*fsz[1])
        fg,bg = fgbg(colors[ufg[x]],x)
        tx = font.render(i,True,fg,bg)
        scr.blit(tx,cpos)
    for x,r in enumerate(content):
        for y,i in enumerate(r):
            cpos = ((x)*fsz[0],(y+1)*fsz[1])
            tx = font.render(i,True,colors[cfg[x][y]],colors[cbg[x][y]])
            scr.blit(tx,cpos)
    cpos = (curp[0]*fsz[0],(curp[1]+1)*fsz[1])
    tx = font.render("_",True,colors[cfg[x][y]])
    scr.blit(tx,cpos)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if md == mode.text:
                if e.key == pygame.K_BACKSPACE:
                    curp = posWrap(curp,-1)
                    content[curp[0]][curp[1]] = " "
                elif e.key == pygame.K_LEFT: curp = posWrap(curp,-1)
                elif e.key == pygame.K_RIGHT: curp = posWrap(curp,1)
                elif e.key == pygame.K_UP: curp = posWrap(curp,0,-1)
                elif e.key == pygame.K_DOWN: curp = posWrap(curp,0,1)
                elif e.key == pygame.K_RETURN: curp = returnLn(curp)
                else:
                    content[curp[0]][curp[1]] = e.unicode
                    curp = posWrap(curp,1)
    pygame.display.flip()