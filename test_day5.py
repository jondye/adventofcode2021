from day5 import *
from io import StringIO
import pytest


def test_read_input():
    f = StringIO("60,28 -> 893,861\n934,945 -> 222,233\n")
    lines = read_input(f)
    assert lines[0] == ((60, 28), (893, 861))
    assert lines[1] == ((934, 945), (222, 233))


def test_lines():
    floor = OceanFloor([((0, 9), (5, 9))])
    assert floor.floor[0][9] == 1
    assert floor.floor[1][9] == 1
    assert floor.floor[2][9] == 1
    assert floor.floor[3][9] == 1
    assert floor.floor[4][9] == 1
    assert floor.floor[5][9] == 1

    assert floor.floor[0][8] == 0
    assert floor.floor[2][8] == 0
    assert floor.floor[6][9] == 0


def test_day5_1():
    lines = [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2)),
    ]
    floor = OceanFloor(lines)
    assert floor.overlapping_points() == 5