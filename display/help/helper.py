from rich.console import Console
from rich.markdown import Markdown

__all__ = ['Helper']


class Helper:
    def __init__(self, label, delay):
        self.console = Console()

    def run(self):
        with open("./display/help/help.md", "r+") as f:
            self.console.print(Markdown(f.read()))

        input()
