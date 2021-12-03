from day3_2 import *

numbers = [[int(x) for x in l] for l in ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']]

def test_oxygen_generator_rating():
    assert oxygen_generator_rating(numbers) == 23

def test_co2_scrubber_rating():
    assert co2_scrubber_rating(numbers) == 10

def test_highest_bit():
    assert highest_bit([[0,0], [0,0], [1,0]], 0) == 0