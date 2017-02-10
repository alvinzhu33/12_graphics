from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

for y in range(0,500,5):
    draw_line(screen, 0, 0, 500, y, color)
display(screen)
save_extension(screen, 'img.png')
