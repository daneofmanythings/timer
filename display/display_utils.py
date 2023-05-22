import os
import shutil
from enum import Enum


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def color_text(text: str, r: int, g: int, b: int) -> str:
    '''Sets a string to a color specified by RGB values'''
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def calc_term_offset() -> tuple[int, int]:
    x, y = shutil.get_terminal_size()
    return x // 2, y // 2 - 1


def calc_string_offset(string) -> int:
    # if len(string) % 2 == 0:
    #     return len(string) // 2
    return 1 + len(string) // 2


def calc_time(delay: int) -> tuple[int, int]:
    minutes, seconds = divmod(delay, 60)
    minutes, seconds = f"{minutes}".zfill(2), f"{seconds}".zfill(2)
    return minutes, seconds
