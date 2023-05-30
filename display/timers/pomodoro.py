from concurrent.futures import ThreadPoolExecutor
import time
import display.display_utils as dutils
from display.timers.timer import Timer

__all__ = ['Pomodoro']


class Pomodoro(Timer):

    # Added whitespace is to accomodate the color information in the string
    # so that the offsets line up correctly
    working_label = ' ' * 25 + dutils.color_text(
        'Working...', *dutils.Color.SOFT_GREEN.value)
    resting_label = ' ' * 24 + dutils.color_text(
        'Resting!', *dutils.Color.DARK_PINK.value)
    break_label = ' ' * 23 + dutils.color_text(
        'Break Time!!', *dutils.Color.SOFT_YELLOW.value)

    def __init__(self, label_string, delay):
        super().__init__(Pomodoro.working_label, 25 * 60)

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

    def pomodoro(self, status, intervals):
        if self.delay == 0:
            if status is True:
                intervals += 1
                status = False
                if not intervals % 4:
                    self.label = Pomodoro.break_label
                    self.delay = 30 * 60
                else:
                    self.label = Pomodoro.resting_label
                    self.delay = 5 * 60
            else:
                self.label = Pomodoro.working_label
                status = True
                self.delay = 25 * 60

        return status, intervals

    def run(self):

        pool = ThreadPoolExecutor(3)
        def sleeper(): return time.sleep(1)
        working = True
        intervals_completed = 0

        try:
            while True:

                timer = pool.submit(sleeper)
                working, intervals_completed = pool.submit(
                    self.pomodoro, working, intervals_completed).result()
                pool.submit(self.display_timer)
                self.delay -= 1
                timer.result()
        except KeyboardInterrupt:
            pass

        pool.shutdown()
