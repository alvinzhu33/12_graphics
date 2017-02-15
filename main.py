from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#for y in range(0,500,5):
#    draw_line(screen, 0, 0, 500, y, color)
draw_line(screen, 250, 250, 500, 300, [255,255,255])#1
draw_line(screen, 250, 250, 300, 500, color)#2
draw_line(screen, 250, 250, 300, 0, color)#7
draw_line(screen, 250, 250, 500, 200, color)#8
display(screen)
save_extension(screen, 'img.png')
