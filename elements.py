import pygame

fsz = (0,0)

font:pygame.font.Font = None
btmBar =0

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


def chngSEL(SEL,sel):
    SEL.x,SEL.y = sel.x*fsz[0],sel.y*fsz[1]
    SEL.width,SEL.height = sel.width*fsz[0],sel.height*fsz[1]

class tool:
    def __init__(self,text,id,pos):
        self.text =text
        self.id =id
        self.pos = pos
        self.rect = font.render(self.text,True,(255,255,255)).get_rect()
        self.rect.y = btmBar
        self.rect.x = fsz[0]*pos
        self.col = (255,255,255)
        
    def draw(self,scr:pygame.Surface,sel):
        scr.blit(font.render(self.text,True,self.col,colors[15-int(sel==self.id)]),self.rect)
        


class element:
    bg = 1
    def __init__(self,rect:pygame.Rect,bg=1) -> None:
        self.rect:pygame.Rect = rect
        self.rectE:pygame.Rect = rect.copy()
        chngSEL(self.rectE,self.rect)
        self.content = [("").rjust(rect.width," ")for i in range(rect.height)]
        self.color = bg
        self.fg = 15
    def draw(self,scr:pygame.Surface,out):
        #scr.fill(colors[self.color],self.rectE)
        
        for i,l in enumerate(self.content):
            lpos = self.rectE.copy()
            lpos.y += i*fsz[1]
            lntx = font.render(l,True,colors[self.fg],colors[self.color])
            scr.blit(lntx,lpos)
        if out:
            pygame.draw.rect(scr,(255,255,255),self.rectE,2)
    
    def editText(self,text:str,ln):
        if len(text) <= self.rect.width-2:
            self.content[ln] = text.center(self.rect.width," ")




class button(element):
    bg = 13
    def __init__(self, rect: pygame.Rect) -> None:
        super().__init__(rect, self.bg)




elems = [button,element]