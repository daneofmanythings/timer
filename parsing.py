# optional argvs :
# --timer, -t : increasing timer setting
# --seconds, -s : specify seconds
# --help, -h : print help options

from enum import Enum, auto


class Optionals(Enum):
    TIMER = auto()
    SECONDS = auto()
    HELP = auto()


def filter_optionals(argvs: list[str]) -> list[list[str]]:
    optionals = list()
    result = list()
    for i, argv in enumerate(argvs):
        if argv[0] == '-':
            optionals.append(argvs.pop(i))
    result.append(argvs)
    result.append(optionals)
    return result
