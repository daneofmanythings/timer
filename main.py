import time
import sys
import display
import utils


def main():
    utils.clear_screen()
    try:
        label_string = str(sys.argv[1])
    except IndexError:
        label_string = "TIMER"
    try:
        minutes = int(sys.argv[2])
    except IndexError:
        minutes = None
    try:
        seconds = int(sys.argv[3])
    except IndexError:
        seconds = None

    start = time.perf_counter()

    display.run_timer(minutes, seconds, label_string)
    total_time = time.perf_counter() - start

    display.timer_complete(label_string)

    # file = "~/code/projects/timer/sounds/beep.wav"

    utils.clear_screen()

    print(f'timer took {total_time} to complete')


if __name__ == "__main__":
    main()
