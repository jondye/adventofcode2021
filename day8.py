#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import repeat


class Decoder:
    def __init__(self, observations):
        pass

    def decode(self, code):
        length = len(code)
        if length == 2:
            return 1
        if length == 4:
            return 4
        if length == 3:
            return 7
        if length == 7:
            return 8
        return None


def day8_1(data):
    return sum(1
               for observations, codes in data
               for c, d in zip(codes, repeat(Decoder(observations))) if d.decode(c) in (1, 4, 7, 8))


def parse_line(l):
    observations, codes = l.split('|')
    return (observations.split(), codes.split())


def main():
    with open('input8.txt') as f:
        data = [parse_line(l) for l in f.readlines()]
    print(f"1, 4, 7 and 8 appear {day8_1(data)} times")


if __name__ == '__main__':
    main()
