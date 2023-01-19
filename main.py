import curses
import asyncio
import time


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

def draw(canvas):
    row, column = (5, 5)
    canvas.border()
    coroutine = blink(canvas, row, column)
    while True:
        try:
            coroutine.send(None)
            canvas.refresh()
            time.sleep(5)
        except StopIteration:
            break

  
# def blink_star(canvas):
#     row, column = (5, 5)
#     canvas.border()
#     while True:
#         canvas.addstr(row, column, '*', curses.A_DIM)
#         time.sleep(2)
#         canvas.refresh()
#         canvas.addstr(row, column, '*')
#         time.sleep(0.3)
#         canvas.refresh()
#         canvas.addstr(row, column, '*', curses.A_BOLD)
#         time.sleep(0.5)
#         canvas.refresh()
#         canvas.addstr(row, column, '*')
#         time.sleep(0.3)
#         canvas.refresh()

  
if __name__ == '__main__':
    curses.update_lines_cols()
    # curses.initscr()
    # curses.curs_set(False)
    curses.wrapper(draw)
    
    