import time
import utils
import shutil
import threading

GREEN = (0, 255, 0)
RED = (255, 0, 0)


def color_text(text: str, r: int, g: int, b: int) -> str:
    '''Sets a string to a color specified by RGB values'''
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def calc_term_offset() -> tuple[int, int]:
    x, y = shutil.get_terminal_size()
    return x // 2, y // 2 - 2


def calc_string_offset(string) -> int:
    if len(string) % 2 == 0:
        return len(string) // 2
    return 1 + len(string) // 2


def calc_time(delay: int, *color) -> tuple[int, int]:
    minutes, seconds = divmod(delay, 60)
    minutes, seconds = f"{minutes}".zfill(2), f"{seconds}".zfill(2)
    seconds = color_text(seconds, *color) if delay < 60 else seconds
    minutes = color_text(minutes, *color) if delay < 60 else minutes
    return minutes, seconds


def display_timer(delay, color, label_string) -> None:
    x, y = calc_term_offset()
    s = calc_string_offset(label_string)

    minutes, seconds = calc_time(delay, *color)
    timer = f'>>> {minutes} : {seconds} <<<'
    t = 8
    # timer = '>>> {minutes} : {seconds} <<<'
    # t = calc_string_offset(timer)

    label_x_adj = ' ' * (x - s)
    timer_x_adj = ' ' * (x - t)
    # x_adj = ' ' * x
    y_adj = '\n' * y
    dstring = f'{y_adj}{label_x_adj}{label_string}\n{timer_x_adj}{timer}'
    utils.clear_screen()
    print(dstring)


# TODO: Look into refactor to further reduce drift
def run_timer(minutes, seconds, label_string):
    minutes = 5 if minutes is None else minutes
    seconds = 0 if seconds is None else seconds

    delay = 0
    delay += minutes * 60
    delay += seconds

    def sleeper(): return time.sleep(1)
    def timer(): return display_timer(delay, RED, label_string)

    while delay:
        t1 = threading.Thread(target=sleeper)
        t2 = threading.Thread(target=timer)

        delay -= 1
        t1.start()
        t2.start()
        t1.join()
        t2.join()


def timer_complete(label_string):
    delay = 0
    label_string = label_string + ' (COMPLETE)'
    def sleeper(): return time.sleep(1)
    def timer(): return display_timer(delay, GREEN, label_string)

    try:
        while True:
            t1 = threading.Thread(target=sleeper)
            t2 = threading.Thread(target=timer)

            delay += 1
            t1.start()
            t2.start()
            t1.join()
            t2.join()
    except KeyboardInterrupt:
        pass
