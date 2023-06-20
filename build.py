import pygame,subprocess,os,elements

def build(c,fg,bg):
    rows = []
    for i,r in enumerate(c):
        Rc = ""
        Rfg,Rbg = "",""
        for I,itm in enumerate(r):
            Rc+= (itm)
            Rfg +=hex(fg[i][I]).removeprefix("0x")
            Rbg +=hex(bg[i][I]).removeprefix("0x")
        rows.append((Rc,Rfg,Rbg))
    
    blits = ""
    #print(rows)
    for C,f,b in (rows):
        blits += f'term.blit("{C}","{f}","{b}")\n'

    fileTxt = f"""term.setCursorPos(1,1)
term.clear()
{blits}
"""
    with open("computer\\0\\code.lua","w") as f:
        f.write(fileTxt)

    subprocess.run(f"CraftOS-PC --directory {os.curdir}")
    
