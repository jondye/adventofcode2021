from day7 import *
import pytest

positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_day7_1():
    assert day7_1(positions) == 37


def test_day7_2():
    assert day7_2(positions) == 168


def test_best_position_by_distance():
    c = Crabs(positions)
    assert c.best_position_by_distance() == 2


def test_distance_from():
    c = Crabs(positions)
    assert c.distance_from(2) == [14, 1, 0, 2, 2, 0, 5, 1, 0, 12]


def test_best_position_by_fuel():
    c = Crabs(positions)
    assert c.best_position_by_fuel() == 5


def test_fuel_costs_to():
    c = Crabs(positions)
    assert c.fuel_costs_to(5) == [66, 10, 6, 15, 1, 6, 3, 10, 6, 45]


def test_triangular_numbers():
    n = TriangularNumbers()
    assert n[6] == 21
    assert n[5] == 15
    assert n[4] == 10
    assert n[3] == 6
    assert n[2] == 3
    assert n[1] == 1
    assert n[0] == 0
