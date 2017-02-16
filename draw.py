from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if(x0<x1):
        a = y1 - y0
        b = -(x1 - x0)
        c = -b*b
        #print(str(a) + " " + str(b))

        #Oct 1
        if(a<=-b and a>=0 and b<=0):
            #print("1\n")
            d = 2*a + b

            while x0<x1:
                plot(screen, color, x0, y0)
                if d>0:
                    y0+=1
                    d+=2*b

                x0+=1
                d+=2*a

        #Oct 2
        if(a>-b and a>0 and b<0):
            #print("2\n")
            d = 2*b + a

            while y0<y1:
                plot(screen, color, x0, y0)
                if d<0:
                    x0+=1
                    d+=2*a

                y0+=1
                d+=2*b

        #Oct 7
        if(a<=b and a<=0 and b<=0):
            #print("7\n")
            d = -2*b + a

            while y0>y1:
                plot(screen, color, x0, y0)
                if d>0:
                    x0+=1
                    d+=2*a

                y0-=1
                d-=2*b

        #Oct 8
        if(a>b and a<0 and b<0):
            #print("8\n")
            d = 2*a - b

            while x0<x1:
                plot(screen, color, x0, y0)
                if d<0:
                    y0-=1
                    d-=2*b

                x0+=1
                d+=2*a

    else:
        a = y0 - y1
        b = -(x0 - x1)
        c = -b*b
        #print(str(a) + " " + str(b))

        #Oct 5
        if(a<=-b and a>=0 and b<0):
            #print("5\n")
            d = 2*a + b

            while x1<=x0:
                plot(screen, color, x1, y1)
                if d>0:
                    y1+=1
                    d+=2*b

                x1+=1
                d+=2*a

        #Oct 6
        if(a>=-b and a>=0 and b<=0):
            #print("6\n")
            d = 2*b + a

            while y1<=y0:
                plot(screen, color, x1, y1)
                if d<0:
                    x1+=1
                    d+=2*a

                y1+=1
                d+=2*b

        #Oct 3
        if(-a>=-b and a<=0 and b<=0):
            #print("3\n")
            d = -2*b + a

            while y1>=y0:
                plot(screen, color, x1, y1)
                if d>0:
                    x1+=1
                    d+=2*a

                y1-=1
                d-=2*b

        #Oct 4
        if(-a<-b and a<0 and b<0):
            #print("4\n")
            d = 2*a - b

            while x1<=x0:
                plot(screen, color, x1, y1)
                if d<0:
                    y1-=1
                    d-=2*b

                x1+=1
                d+=2*a
