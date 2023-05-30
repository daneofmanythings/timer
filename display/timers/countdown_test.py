from concurrent.futures import ThreadPoolExecutor
import time
# import display.display_utils as dutils
from display.timers.timer import Timer

__all__ = ['CountdownTest']


class CountdownTest(Timer):

    def __init__(self, label_string, delay):
        super().__init__(label_string, delay)

    def display_timer(self):
        result = self.display_string.format(
            self.vert_adjust(),
            self.label_hori_adjust(),
            self.label,
            self.timer_hori_adjust(),
            self.timer_string.format(*self.calc_timer())
        )
        self.clear_environment()
        print(result)

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
