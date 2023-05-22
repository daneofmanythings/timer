import time
import sys
from display.timers import Countdown
import utils
# import parsing


def main():
    utils.clear_screen()
    # args = parsing.filter_optionals(sys.argv)
    try:
        label_string = str(sys.argv[1])
    except IndexError:
        label_string = "TIMER"
    try:
        minutes = int(sys.argv[2])
    except IndexError:
        minutes = 0
    try:
        seconds = int(sys.argv[3])
    except IndexError:
        seconds = 5

    minutes *= 60
    delay = minutes + seconds

    start = time.perf_counter()

    timer = Countdown(label_string, delay)
    timer.run()
    # timers.run_timer_countdown(minutes, seconds, label_string)
    # display.run_timer_countup(label_string)

    total_time = time.perf_counter() - start

    utils.clear_screen()

    print(f'timer took {total_time} to complete')


if __name__ == "__main__":
    main()
