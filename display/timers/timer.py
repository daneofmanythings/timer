import display.display_utils as dutils

__all__ = ['Timer']


class Timer:

    timer_string = '  >>> {0} : {1} <<<'
    display_string = '{0}{1}{2}\n{3}{4}'

    def __init__(self, label_string, delay):
        self.delay = delay
        self.label = label_string

    def clear_environment(self):
        dutils.clear_terminal()

    def color_text(self, text, color):
        return dutils.color_text(text, *color)

    def environment_offset(self):
        return dutils.calc_term_offset()

    def timer_offset(self) -> int:
        return dutils.calc_string_offset(self.timer_string)

    def calc_timer(self):
        return dutils.calc_time(self.delay)

    def label_offset(self) -> int:
        return dutils.calc_string_offset(self.label)

    def vert_adjust(self):
        _, y = self.environment_offset()
        return '\n' * y

    def timer_hori_adjust(self) -> int:
        x, _ = self.environment_offset()
        return ' ' * (x - self.timer_offset())

    def label_hori_adjust(self) -> int:
        x, _ = self.environment_offset()
        return ' ' * (x - self.label_offset())
