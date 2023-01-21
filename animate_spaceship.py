import time
from curses_tools import draw_frame

with open('rocket_frame_1.txt', 'r') as frame_1:
    rocket_frame_1 = frame_1.read()

with open('rocket_frame_1.txt', 'r') as frame_2:
    rocket_frame_2 = frame_2.read()

row, column = 20, 20
canvas.border()

draw_frame(canvas, row, column, rocket_frame_1)
canvas.refresh()

time.sleep(1)

draw_frame(canvas, row, column, rocket_frame_1, negative=True)
draw_frame(canvas, row, column, rocket_frame_2)
canvas.refresh()

time.sleep(1)
