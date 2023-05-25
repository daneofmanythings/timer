# optional argvs :
# --stopwatch, -s : use stopwatch mode
# --help, -h : print help options
# (number) : minutes
# XX:XX : full time

from enum import Enum, auto
import display


class Optionals(Enum):
    COUNTDOWN = display.Countdown
    STOPWATCH = display.Stopwatch
    HELP = auto()


class Duration:
    def __init__(self, input):
        self.input = input

    def __repr__(self):
        return f'{self.input}'


class ArgvParser:
    def __init__(self, argvs):
        self.argvs = argvs
        self.duration = 0
        self.mode = Optionals.COUNTDOWN
        self.title = ""

        self.parser()

    def parser(self):
        for argv in self.argvs:
            if self.duration == 0 and (len(argv.split(":")) > 1 or argv.isdigit()):
                self.duration += int(argv.split(":")[0]) * 60
                try:
                    self.duration += int(argv.split(":")[1])
                except IndexError:
                    pass
            elif argv in ('-h', '--help'):
                self.mode = Optionals.HELP
            elif argv in ('-s', '--stopwatch'):
                self.mode = Optionals.STOPWATCH
            else:
                if not self.title:
                    self.title = argv

    def parsed_args(self):
        return self.mode.value, self.title, self.duration


def main():
    args = ArgvParser(['laundry', '-s', '2'])

    print(args.parsed_args())


if __name__ == "__main__":
    main()
