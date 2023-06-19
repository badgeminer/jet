import pygame,sys
pygame.init()

font  = pygame.font.Font("SpaceMono-Regular.ttf",15)

fsz = font.size("E")
uisz =(51,19)
sz = ((uisz[0]+1)*fsz[0],(uisz[1]+1)*fsz[1])
print(sz)
scr = pygame.display.set_mode(sz)

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

curp = [0,0]

while True:
    scr.fill((0,0,0))
    for x,r in enumerate(content):
        for y,i in enumerate(r):
            cpos = ((x)*fsz[0],(y+1)*fsz[1])
            tx = font.render(i,True,colors[cfg[x][y]],colors[cbg[x][y]])
            scr.blit(tx,cpos)
    cpos = ((x)*fsz[0],(y+1)*fsz[1])
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()