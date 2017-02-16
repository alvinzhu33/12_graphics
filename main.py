from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#for y in range(0,500,5):
#    draw_line(screen, 0, 0, 500, y, color)

draw_line(screen, 250, 250, 500, 250, [75,75,75])
draw_line(screen, 250, 250, 500, 300, [255,0,0])#1R
draw_line(screen, 250, 250, 500, 500, [100,100,100])#1.5
draw_line(screen, 250, 250, 300, 500, [255,153,0])#2O

draw_line(screen, 250, 250, 250, 500, [125,125,125])
draw_line(screen, 250, 250, 200, 500, [255,255,0])#3Y
draw_line(screen, 250, 250, 0, 500, [150,150,150])#2O
draw_line(screen, 250, 250, 0, 300, [0,255,0])#4G

draw_line(screen, 250, 250, 0, 250, [175,175,175])
draw_line(screen, 250, 250, 0, 200, [0,255,255])#5C
draw_line(screen, 250, 250, 0, 0, [200,200,200])
draw_line(screen, 250, 250, 200, 0, [0,0,255])#6B

draw_line(screen, 250, 250, 250, 0, [225,225,225])
draw_line(screen, 250, 250, 300, 0, [255,0,255])#7M
draw_line(screen, 250, 250, 500, 0, [250,250,250])
draw_line(screen, 250, 250, 500, 200, [125,114,57])#8W

display(screen)
save_extension(screen, 'img.png')
