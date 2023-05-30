from concurrent.futures import ThreadPoolExecutor
import time
# import display.display_utils as dutils
from display.timers.timer import Timer

__all__ = ['CountdownTest']


class CountdownTest(Timer):

    def __init__(self, label_string, delay):
        super().__init__(label_string, delay)

    def run(self):

        def sleeper(): return time.sleep(1)
        pool = ThreadPoolExecutor(3)

        try:
            while self.delay:
                timer = pool.submit(sleeper)
                pool.submit(self.display_timer)

                timer.result()

                self.delay -= 1

        except KeyboardInterrupt:
            pool.shutdown()
