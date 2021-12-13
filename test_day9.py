from day9 import *
import copy
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


def test_point():
    p = Point(heightmap)
    assert p.value == 2
    assert sorted(x.value for x in p.neighbours) == [1, 3]
    p = Point(heightmap, 1, 0)
    assert p.value == 1
    assert sorted(x.value for x in p.neighbours) == [2, 9, 9]
    p = Point(heightmap, 9, 0)
    assert p.value == 0
    assert sorted(x.value for x in p.neighbours) == [1, 1]
    p = Point(heightmap, 0, 4)
    assert p.value == 9
    assert sorted(x.value for x in p.neighbours) == [8, 8]
    p = Point(heightmap, 9, 4)
    assert p.value == 8
    assert sorted(x.value for x in p.neighbours) == [7, 9]


def test_day9_2():
    assert day9_2(heightmap) == 1134


def test_find_basins():
    assert sorted(find_basins(heightmap)) == [3, 9, 9, 14]


def test_iterator():
    p = iter(Point(heightmap))
    assert p.value == 2
    assert sorted(x.value for x in p.neighbours) == [1, 3]
    next(p)
    assert p.value == 1
    assert sorted(x.value for x in p.neighbours) == [2, 9, 9]
    for _ in range(8):
        next(p)
    assert p.value == 0
    assert sorted(x.value for x in p.neighbours) == [1, 1]
    for _ in range(31):
        next(p)
    assert p.value == 9
    assert sorted(x.value for x in p.neighbours) == [8, 8]
    for _ in range(9):
        next(p)
    assert p.value == 8
    assert sorted(x.value for x in p.neighbours) == [7, 9]
    with pytest.raises(StopIteration):
        next(p)


def test_measure_basin():
    top_left = Point(copy.deepcopy(heightmap), 0, 0)
    assert measure_basin(top_left) == 3
