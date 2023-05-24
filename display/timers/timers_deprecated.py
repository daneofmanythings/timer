import time
import utils
import threading
from display.display_utils import (
    calc_string_offset,
    calc_term_offset,
    calc_time,
    color_text,
    Color)

__all__ = ['display_timer_countdown', 'display_timer_countup']


def display_timer_countdown(delay, color, label_string) -> None:
    x, y = calc_term_offset()
    s = calc_string_offset(label_string)

    minutes, seconds = calc_time(delay)
    minutes = color_text(minutes, *color) if delay < 60 else minutes
    seconds = color_text(seconds, *color) if delay < 60 else seconds
    timer = f'>>> {minutes} : {seconds} <<<'
    t = 8  # hard coded the offset for the timer. f-string wasn't playing nicely

    label_x_adj = ' ' * (x - s)
    timer_x_adj = ' ' * (x - t)
    y_adj = '\n' * y
    dstring = f'{y_adj}{label_x_adj}{label_string}\n{timer_x_adj}{timer}'
    utils.clear_screen()
    print(dstring)


# TODO: Look into refactor to further reduce drift
def run_timer_countdown(minutes, seconds, label_string):
    minutes = 5 if minutes is None else minutes
    seconds = 0 if seconds is None else seconds

    delay = 0
    delay += minutes  # * 60
    delay += seconds

    def sleeper(): return time.sleep(1)

    def timer_cowndown(): return display_timer_countdown(
        delay, Color.RED.value, label_string)

    def timer_complete(): return display_timer_countdown(
        delay, Color.GREEN.value, label_string + " (COMPLETE)")

    try:
        while delay:
            t1 = threading.Thread(target=sleeper)
            t2 = threading.Thread(target=timer_cowndown)

            delay -= 1
            t1.start()
            t2.start()
            t1.join()
            t2.join()

        while True:
            t1 = threading.Thread(target=sleeper)
            t2 = threading.Thread(target=timer_complete)

            delay += 1
            t1.start()
            t2.start()
            t1.join()
            t2.join()
    except KeyboardInterrupt:
        pass


def display_timer_countup(delay, label_string) -> None:
    x, y = calc_term_offset()
    s = calc_string_offset(label_string)

    minutes, seconds = calc_time(delay)
    timer = f'>>> {minutes} : {seconds} <<<'
    t = 8  # hard coded the offset for the timer. f-string wasn't playing nicely

    label_x_adj = ' ' * (x - s)
    timer_x_adj = ' ' * (x - t)
    y_adj = '\n' * y
    dstring = f'{y_adj}{label_x_adj}{label_string}\n{timer_x_adj}{timer}'
    utils.clear_screen()
    print(dstring)


def run_timer_countup(label_string):
    delay = 0

    def sleeper(): return time.sleep(1)
    def counter(): return display_timer_countup(delay, label_string)

    try:
        while True:
            t1 = threading.Thread(target=sleeper)
            t2 = threading.Thread(target=counter)

            t1.start()
            t2.start()
            t1.join()
            t2.join()
            delay += 1

    except KeyboardInterrupt:
        pass