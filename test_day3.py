from day3_2 import *

numbers = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
]

def test_oxygen_generator_rating():
    assert oxygen_generator_rating(numbers) == 23

def test_co2_scrubber_rating():
    assert co2_scrubber_rating(numbers) == 10

def test_split():
    assert split([[0], [1], [0]], 0)[0] == [[0], [0]]
    assert split([[0], [1], [0]], 0)[1] == [[1]]
    assert split(numbers, 0)[0] == [[0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 0]]