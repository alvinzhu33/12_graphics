from display import *

def draw_lineQ1( screen, x0, y0, x1, y1, color ):
    a = y1 - y0
    b = -(x1 - x0)
    c = -b*b

    if(a<-b and a>0 and b<0):
        d = 2*a + b

        while x0<=x1:
            plot(screen, color, x0, y0)
            if d>0:
                y0+=1
                d+=2*b
            x0+=1
            d+=2*a

    if(a>-b and a>0 and b<0):
        d = 2*b + a

        while x0<=x1:
            plot(screen, color, x0, y0)
            if d<0:
                y0+=1
                d+=2*a
            x0+=1
            d+=2*b

    if(a<b and a<0 and b<0):
        d = 2*a - b

        while x0<=x1:
            plot(screen, color, x0, y0)
            if d<0:
                y0-=1
                d-=2*b
            x0+=1
            d+=2*a
