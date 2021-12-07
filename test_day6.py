from day6 import *
import pytest

def test_day6_1():
    f = Fish([3,4,3,1,2])
    f.time_passes(18)
    assert f.count() == 26
    f.time_passes(62)
    assert f.count() == 5934

def test_time_passes():
    f = Fish([3,4,3,1,2])
    assert f.state == [3, 4, 3, 1, 2]
    f.time_passes(1)
    assert f.state == [2, 3, 2, 0, 1]
    f.time_passes(1)
    assert f.state == [1, 2, 1, 6, 0, 8]

    f.time_passes(2)
    assert f.state == [6, 0, 6, 4, 5, 6, 7, 8, 8]