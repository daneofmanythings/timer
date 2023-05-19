import time
import sys
import display
import utils


def main():
    utils.clear_screen()
    try:
        minutes = int(sys.argv[1])
    except IndexError:
        minutes = None
    try:
        seconds = int(sys.argv[2])
    except IndexError:
        seconds = None

    start = time.perf_counter()

    display.run_timer(minutes, seconds)
    display.timer_complete()

    # file = "~/code/projects/timer/sounds/beep.wav"

    utils.clear_screen()

    total_time = time.perf_counter() - start

    print('TIMER COMPLETE')
    print(f'took {total_time}')


if __name__ == "__main__":
    main()
