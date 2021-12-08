#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import repeat


class Decoder:
    def __init__(self, observations):
        self.segment_frequency = {
            letter: sum(1 for code in observations if letter in code) for letter in 'abcdefg'}
        self.lookup = {
            42: 0, 17: 1, 34: 2, 39: 3, 30: 4, 37: 5, 41: 6, 25: 7, 49: 8, 45: 9}

    def decode(self, code):
        segment_frequency = sum(
            self.segment_frequency[letter] for letter in code)
        return self.lookup[segment_frequency]

    def decode_number(self, digits):
        return sum(self.decode(d) * (10**exp) for exp, d in enumerate(reversed(digits)))


def day8_1(data):
    return sum(1
               for observations, codes in data
               for c, d in zip(codes, repeat(Decoder(observations))) if d.decode(c) in (1, 4, 7, 8))


def day8_2(data):
    return sum(Decoder(observations).decode_number(codes) for observations, codes in data)


def parse_line(l):
    observations, codes = l.split('|')
    return (observations.split(), codes.split())


def main():
    with open('input8.txt') as f:
        data = [parse_line(l) for l in f.readlines()]
    print(f"1, 4, 7 and 8 appear {day8_1(data)} times")
    print(f"total of all codes is {day8_2(data)}")


if __name__ == '__main__':
    main()
