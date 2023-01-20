import curses
import asyncio
import time
from random import randint, choice
from fire_animation import fire

TIC_TIMEOUT = 0.1


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(50):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(20):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(20):
            await asyncio.sleep(0)
        time.sleep(randint(1, 15))


def draw(canvas):
    canvas.border()
    y, x = curses.window.getmaxyx(canvas)
    symbols = ('+', ':', '.', '*')
    coroutines = []
    edge = 3

    for _ in range(150):
        row, column = (randint(edge, y - edge), randint(edge, x - edge))
        coroutines.append(blink(canvas, row, column, choice(symbols)))
        coroutines.append(fire(canvas, (y - edge) / 2, (x - edge) / 2))

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
                canvas.refresh()
            except StopIteration:
                break
            except RuntimeError:
                break
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.initscr()
    curses.curs_set(False)
    curses.wrapper(draw)
