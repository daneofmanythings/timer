from concurrent.futures import ThreadPoolExecutor
import time
from display.timers.timer import Timer

__all__ = ['Stopwatch']


class Stopwatch(Timer):

    def __init__(self, label_string, delay):
        super().__init__(label_string, 0)

    def run(self):

        pool = ThreadPoolExecutor()
        def sleeper(): return time.sleep(1)

        try:
            while True:

                timer = pool.submit(sleeper)
                pool.submit(self.display_timer)
                timer.result()
                self.delay += 1

        except KeyboardInterrupt:
            pool.shutdown()
