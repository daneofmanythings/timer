import threading
import time
from display.timers.timer import Timer

__all__ = ['Stopwatch']


class Stopwatch(Timer):

    def __init__(self, label_string, delay):
        super().__init__(label_string, 0)

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

        try:
            while True:

                t1 = threading.Thread(target=sleeper)
                t2 = threading.Thread(target=self.display_timer)

                t1.start()
                t2.start()
                t1.join()
                t2.join()

                self.delay += 1
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    label = 'testss'
    delay = 1
    timer = Stopwatch(label, delay)
    timer.run()
