#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain


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


def main():
    with open('input9.txt') as f:
        heightmap = [[int(x) for x in line.strip()] for line in f.readlines()]
    print(f"sum of risk levels is {day9_1(heightmap)}")


if __name__ == '__main__':
    main()
