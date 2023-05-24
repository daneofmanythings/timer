import threading
import time
import display.display_utils as dutils
from display.timers.timer import Timer

__all__ = ['Countdown']


class Countdown(Timer):

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

        try:
            while self.delay:
                t1 = threading.Thread(target=sleeper)
                t2 = threading.Thread(target=self.display_timer)

                self.delay -= 1
                t1.start()
                t2.start()
                t1.join()
                t2.join()

            while True:
                if self.delay == 0:
                    s = self.color_text(
                        ' (COMPLETE)', dutils.Color.GREEN.value)
                    self.label += s

                    # janky measure to counteract the string data from coloring
                    self.label = ' ' * 20 + self.label

                t1 = threading.Thread(target=sleeper)
                t2 = threading.Thread(target=self.display_timer)

                self.delay += 1
                t1.start()
                t2.start()
                t1.join()
                t2.join()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    label = 'testss'
    delay = 1
    timer = Countdown(label, delay)
    timer.run()
