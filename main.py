import time
import sys
import utils
import parsing


def main():
    utils.clear_screen()
    start = time.perf_counter()
    parser = parsing.ArgvParser(sys.argv[1:])
    mode, label, duration = parser.parsed_args()

    timer = mode(label, duration)
    timer.run()

    total_time = time.perf_counter() - start

    utils.clear_screen()

    print(f'timer took {total_time} to complete')


if __name__ == "__main__":
    main()
