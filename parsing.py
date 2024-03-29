# optional argvs :
# --stopwatch, -s : use stopwatch mode
# --help, -h : print help options
# (number) : minutes
# XX:XX : full time

from enum import Enum
import display


class Optionals(Enum):
    COUNTDOWN = display.Countdown
    COUNTDOWN_TEST = display.CountdownTest
    STOPWATCH = display.Stopwatch
    POMODORO = display.Pomodoro
    HELP = display.Helper


class ArgvParser:
    def __init__(self, argvs):
        self.argvs = argvs
        self.duration = 0
        self.mode = Optionals.COUNTDOWN
        self.title = ""

        self.parser()

    def parser(self):
        if len(self.argvs) == 0:
            self.mode = Optionals.HELP
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
            elif argv in ('-p', '--pomodoro'):
                self.mode = Optionals.POMODORO
            elif argv in ('-t', '--test'):
                self.mode = Optionals.COUNTDOWN_TEST
            else:
                if not self.title:
                    self.title = argv

    @property
    def parsed_args(self):
        return self.mode.value, self.title, self.duration


def main():
    args = ArgvParser(['laundry', '-s', '2'])

    print(args.parsed_args())


if __name__ == "__main__":
    main()
