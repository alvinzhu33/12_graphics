from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    a = y1 - y0
    b = -(x1 - x0)
    c = -b*b
    d = 2*a + b

    while x0<x1:
        plot(screen, color, x0, y0)
        if d>0:
            y0+=1
            d+=b
        x0+=1
        d+=2*a
