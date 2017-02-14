from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#for y in range(0,500,5):
#    draw_line(screen, 0, 0, 500, y, color)
draw_line(screen, 0, 0, 500, 250, color)
draw_line(screen, 0, 0, 250, 500, color)
draw_line(screen, 0, 500, 250, 0, color)
draw_line(screen, 0, 500, 0, 250, color)
display(screen)
save_extension(screen, 'img.png')
