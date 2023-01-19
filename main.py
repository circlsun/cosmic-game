import curses
import asyncio
import time

TIC_TIMEOUT = 0.1


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
    coroutine_1 = blink(canvas, row, column)
    coroutine_2 = blink(canvas, row, column + 5)
    coroutine_3 = blink(canvas, row, column + 10)
    coroutine_4 = blink(canvas, row, column + 15)
    coroutine_5 = blink(canvas, row, column + 20)

    coroutines = [
        coroutine_1,
        coroutine_2,
        coroutine_3,
        coroutine_4,
        coroutine_5
    ]
    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
                canvas.refresh()
            except StopIteration:
                break
        time.sleep(TIC_TIMEOUT)


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
    curses.initscr()
    curses.curs_set(False)
    curses.wrapper(draw)
