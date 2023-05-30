import os


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


class NoCursor:
    def __enter__(self):
        print('\033[?25l', end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('\033[?25h', end="")
