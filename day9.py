#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain
from pprint import pprint
import copy


class Point:
    def __init__(self, heightmap, x=0, y=0):
        self.heightmap = heightmap
        self.height = len(heightmap)
        self.width = len(heightmap[0])
        self.x = x
        self.y = y

    @property
    def value(self):
        return self.heightmap[self.y][self.x]

    @value.setter
    def value(self, v):
        self.heightmap[self.y][self.x] = v

    def __iter__(self):
        return self

    def __next__(self):
        if self.x + 1 == self.width:
            if self.y + 1 == self.height:
                raise StopIteration
            self.x = 0
            self.y += 1
        else:
            self.x += 1
        return self

    @property
    def neighbours(self):
        return [x for x in (self.north, self.east, self.south, self.west) if x]

    @property
    def north(self):
        return Point(self.heightmap, self.x, self.y - 1) if self.y > 0 else None

    @property
    def east(self):
        return Point(self.heightmap, self.x + 1, self.y) if self.x < self.width - 1 else None

    @property
    def south(self):
        return Point(self.heightmap, self.x, self.y + 1) if self.y < self.height - 1 else None

    @property
    def west(self):
        return Point(self.heightmap, self.x - 1, self.y) if self.x > 0 else None

    def __repr__(self):
        return f"Point<{self.x}, {self.y}>({self.value})"


def measure_basin(p):
    if not p or p.value == 9:
        return 0
    p.value = 9  # Mark as visited
    total = 1 + sum(measure_basin(n) for n in p.neighbours)
    return total


def find_basins(heightmap):
    start = Point(copy.deepcopy(heightmap))
    basins = [measure_basin(p) for p in iter(start)]
    return [b for b in basins if b]


def floor_iterator(heightmap):
    width = len(heightmap[0])
    heightlist = [item for sublist in heightmap for item in sublist]
    north = ([99] * width) + heightlist
    south = heightlist[width:] + ([99] * width)
    east = chain.from_iterable(sublist[1:] + [99] for sublist in heightmap)
    west = chain.from_iterable([99] + sublist[:-1] for sublist in heightmap)
    return zip(heightlist, north, east, south, west)


def day9_1(heightmap):
    return sum(pos + 1 for (pos, *other) in floor_iterator(heightmap) if pos < min(other))


def day9_2(heightmap):
    basins = find_basins(heightmap)
    a, b, c = sorted(basins)[-3:]
    return a * b * c


def main():
    with open('input9.txt') as f:
        heightmap = [[int(x) for x in line.strip()] for line in f.readlines()]
    print(f"sum of risk levels is {day9_1(heightmap)}")
    print(f"product of top 3 areas {day9_2(heightmap)}")


if __name__ == '__main__':
    main()
