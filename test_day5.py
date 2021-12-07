from day5 import *
from io import StringIO
import pytest


def test_read_input():
    f = StringIO("60,28 -> 893,861\n934,945 -> 222,233\n")
    lines = read_input(f)
    assert lines[0] == ((60, 28), (893, 861))
    assert lines[1] == ((934, 945), (222, 233))


def test_horizontal_lines():
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


def test_vertical_lines():
    floor = OceanFloor([((1, 1), (1, 3))])
    assert floor.floor[1][1] == 1
    assert floor.floor[1][2] == 1
    assert floor.floor[1][3] == 1

    assert floor.floor[0][1] == 0
    assert floor.floor[2][1] == 0
    assert floor.floor[1][0] == 0
    assert floor.floor[1][4] == 0


def test_diagonal_lines():
    floor = OceanFloor([((1, 1), (3, 3))], include_diagonal=True)
    assert floor.floor[1][1] == 1
    assert floor.floor[2][2] == 1
    assert floor.floor[3][3] == 1

    assert floor.floor[0][0] == 0
    assert floor.floor[0][1] == 0
    assert floor.floor[2][1] == 0
    assert floor.floor[1][2] == 0
    assert floor.floor[3][2] == 0
    assert floor.floor[2][3] == 0
    assert floor.floor[4][3] == 0
    assert floor.floor[4][4] == 0


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


def test_day5_1():
    floor = OceanFloor(lines)
    assert floor.overlapping_points() == 5


def test_day5_2():
    floor = OceanFloor(lines, include_diagonal=True)
    assert floor.overlapping_points() == 12
