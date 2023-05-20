import threading
import time
import concurrent.futures
# import display


def task1(thread_pool, draw_fn):
    delay = 5
    while delay:
        time.sleep(1)
        thread_pool.map(draw_fn, delay)
        delay -= 1


def task2(delay):
    print(f'task2 fired: {delay}')


def threads(delay):
    def sleeper(): return time.sleep(1)
    def timer(): return task2()

    while delay:
        t1 = threading.Thread(target=sleeper)
        t2 = threading.Thread(target=timer)

        delay -= 1
        t1.start()
        t2.start()
        t1.join()
        t2.join()


def main():
    pool = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    task1(pool, task2)


if __name__ == "__main__":
    main()
