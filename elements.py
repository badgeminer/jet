import pygame

fsz = (0,0)

def chngSEL(SEL,sel):
    SEL.x,SEL.y = sel.x*fsz[0],sel.y*fsz[1]
    SEL.width,SEL.height = sel.width*fsz[0],sel.height*fsz[1]

class element:
    def __init__(self,rect:pygame.Rect) -> None:
        self.rect:pygame.Rect = rect
        self.rectE:pygame.Rect = rect.copy()
        chngSEL(self.rectE,self.rect)
        self.content = [("").rjust(rect.width," ")for i in range(rect.height)]
        self.color = 1