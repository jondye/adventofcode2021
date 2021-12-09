from day9 import *
import pytest

heightmap = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]


def test_day9_1():
    assert day9_1(heightmap) == 15


def test_floor_iterator():
    itr = list(floor_iterator(heightmap))
    assert len(itr) == 50
    assert itr[0] == (2, 99, 1, 3, 99)
    assert itr[1] == (1, 99, 9, 9, 2)
    assert itr[9] == (0, 99, 99, 1, 1)
    assert itr[10] == (3, 2, 9, 9, 99)
    assert itr[40] == (9, 8, 8, 99, 99)
    assert itr[49] == (8, 9, 99, 99, 7)
