from enum import Enum
from typing import Union, Tuple


class Color:
    class Normal(Enum):
        BLACK = 30
        RED = 31
        GREEN = 32
        YELLOW = 33
        BLUE = 34
        MAGENTA = 35
        CYAN = 36
        WHITE = 37

    class Bright(Enum):
        BLACK = 90
        RED = 91
        GREEN = 92
        YELLOW = 93
        BLUE = 94
        MAGENTA = 95
        CYAN = 96
        WHITE = 97


class Style(Enum):
    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINK = 5
    REVERSE = 7
    STRIKETHROUGH = 9


ColorType = Union[Color.Normal, Color.Bright, str, int, Tuple[int, int, int]]
