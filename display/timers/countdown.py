from concurrent.futures import ThreadPoolExecutor
import time
import display.display_utils as dutils
from display.timers.timer import Timer

__all__ = ['Countdown']


class Countdown(Timer):

    complete = dutils.color_text(' (COMPLETE)', *dutils.Color.GREEN.value)

    def __init__(self, label_string, delay):
        super().__init__(label_string, delay)

    def run(self):

        def sleeper(): return time.sleep(1)
        pool = ThreadPoolExecutor()

        try:
            while self.delay:
                timer = pool.submit(sleeper)
                pool.submit(self.display_timer)
                timer.result()
                self.delay -= 1

            self.label = ' ' * 20 + self.label + Countdown.complete

            while True:

                timer = pool.submit(sleeper)
                pool.submit(self.display_timer)
                timer.result()
                self.delay += 1

        except KeyboardInterrupt:
            pool.shutdown()


if __name__ == "__main__":
    label = 'testss'
    delay = 1
    timer = Countdown(label, delay)
    timer.run()
