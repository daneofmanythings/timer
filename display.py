import time
import utils
import shutil
import threading


def colored(r: int, g: int, b: int, text: str) -> str:
    '''Sets a string to a color specified by RGB values'''
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def calc_offset() -> tuple[int, int]:
    x, y = shutil.get_terminal_size()
    return x // 2 - 8, y // 2 - 1


def calc_time_progress(delay: int) -> tuple[int, int]:
    minutes, seconds = divmod(delay, 60)
    minutes, seconds = f"{minutes}".zfill(2), f"{seconds}".zfill(2)
    seconds = colored(255, 0, 0, seconds) if delay < 60 else seconds
    minutes = colored(255, 0, 0, minutes) if delay < 60 else minutes
    return minutes, seconds


def calc_time_complete(delay: int) -> tuple[int, int]:
    minutes, seconds = divmod(delay, 60)
    minutes, seconds = f"{minutes}".zfill(2), f"{seconds}".zfill(2)
    seconds = colored(0, 255, 0, seconds)
    minutes = colored(0, 255, 0, minutes)
    return minutes, seconds


def display_timer_progress(delay) -> None:
    x, y = calc_offset()
    minutes, seconds = calc_time_progress(delay)

    x_adj, y_adj = ' ' * x, '\n' * y
    dstring = f'{y_adj}{x_adj}>>> {minutes} : {seconds} <<<'
    utils.clear_screen()
    print(dstring)


def display_timer_complete(delay) -> None:
    x, y = calc_offset()
    minutes, seconds = calc_time_complete(delay)

    x_adj, y_adj = ' ' * x, '\n' * (y - 1)
    dstring = f'{y_adj}{x_adj}TIMER  COMPLETE\n{x_adj}>>> {minutes} : {seconds} <<<'
    utils.clear_screen()
    print(dstring)

# TODO: Look into refactor to further reduce drift


def run_timer(minutes, seconds):
    minutes = 5 if minutes is None else minutes
    seconds = 0 if seconds is None else seconds

    delay = 0
    delay += minutes  # * 60
    delay += seconds

    def sleeper(): return time.sleep(1)
    def timer(): return display_timer_progress(delay)

    while delay:
        t1 = threading.Thread(target=sleeper)
        t2 = threading.Thread(target=timer)

        delay -= 1
        t1.start()
        t2.start()
        t1.join()
        t2.join()


def timer_complete():
    delay = 0
    def sleeper(): return time.sleep(1)
    def timer(): return display_timer_complete(delay)

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
