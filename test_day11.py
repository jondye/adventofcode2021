from day11 import *

import pytest

octopuses = np.array([
    [5,4,8,3,1,4,3,2,2,3],
    [2,7,4,5,8,5,4,7,1,1],
    [5,2,6,4,5,5,6,1,7,3],
    [6,1,4,1,3,3,6,1,4,6],
    [6,3,5,7,3,8,5,4,7,8],
    [4,1,6,7,5,2,4,6,4,5],
    [2,1,7,6,8,4,1,7,2,1],
    [6,8,8,2,8,8,1,1,3,4],
    [4,8,4,6,8,4,8,5,5,4],
    [5,2,8,3,7,5,1,5,2,6],
])

@pytest.mark.xfail
def test_day11_1():
    assert day11_1(octopuses) == 1656

def test_increase():
    np.testing.assert_array_equal(
        increase(np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]), 1, 1),
        np.array([
            [0,0,0],
            [0,1,0],
            [0,0,0],
        ])
    )
    np.testing.assert_array_equal(
        increase(np.array([
            [0,0,0],
            [0,9,0],
            [0,0,0],
        ]), 1, 1),
        np.array([
            [ 1, 1, 1],
            [ 1,10, 1],
            [ 1, 1, 1],
        ])
    )
    np.testing.assert_array_equal(
        increase(np.array([
            [9,0,0],
            [0,0,0],
            [0,0,0],
        ]), 0, 0),
        np.array([
            [10, 1, 0],
            [ 1, 1, 0],
            [ 0, 0, 0],
        ])
    )
    np.testing.assert_array_equal(
        increase(np.array([
            [0,0,0],
            [0,0,0],
            [0,0,9],
        ]), 2, 2),
        np.array([
            [ 0, 0, 0],
            [ 0, 1, 1],
            [ 0, 1,10],
        ])
    )

def test_one_step():
    np.testing.assert_array_equal(
        step(np.array([
            [0,0,0],
            [0,9,0],
            [0,0,0],
        ])),
        np.array([
            [1,1,1],
            [1,0,1],
            [1,1,1],
        ])
    )

@pytest.mark.xfail
def test_one_step_cascade_flashes():
    np.testing.assert_array_equal(
        step(np.array([
            [1,1,1,1,1],
            [1,9,9,9,1],
            [1,9,1,9,1],
            [1,9,9,9,1],
            [1,1,1,1,1],
        ])),
        np.array([
            [3,4,5,4,3],
            [4,0,0,0,4],
            [5,0,0,0,5],
            [4,0,0,0,4],
            [3,4,5,4,3],
        ])
    )