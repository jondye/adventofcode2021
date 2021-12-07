from day6 import *
import pytest

def test_day6_1():
    f = Fish([3,4,3,1,2])
    f.time_passes(18)
    assert f.count() == 26
    f.time_passes(62)
    assert f.count() == 5934

def test_day6_2():
    f = Fish([3,4,3,1,2])
    f.time_passes(256)
    assert f.count() == 26984457539

def test_time_passes():
    f = Fish([3,4,3,1,2])
    assert f.state == {1: 1, 2: 1, 3: 2, 4: 1}  # [3, 4, 3, 1, 2]
    f.time_passes(1)
    assert f.state == {0: 1, 1: 1, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}  # [2, 3, 2, 0, 1]
    f.time_passes(1)
    assert f.state == {0: 1, 1: 2, 2: 1, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1}  # [1, 2, 1, 6, 0, 8]

    f.time_passes(2)
    assert f.state == {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 3, 7: 1, 8: 2}  # [6, 0, 6, 4, 5, 6, 7, 8, 8]