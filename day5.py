from pprint import pformat, pprint
import re
from collections import defaultdict


class OceanFloor:
    def __init__(self, lines):
        self.lines = lines
        self.floor = defaultdict(lambda: defaultdict(int))
        for ((start_x, start_y), (end_x, end_y)) in lines:
            if (start_x != end_x and start_y != end_y):
                continue
            x_step = 1 if end_x > start_x else -1
            for x in range(start_x, end_x + x_step, x_step):
                y_step = 1 if end_y > start_y else -1
                for y in range(start_y, end_y + y_step, y_step):
                    self.floor[x][y] += 1

    def overlapping_points(self):
        return sum(1 for x in self.floor.values() for y in x.values() if y > 1)


def read_input(f):
    def parse_line(l):
        x1, y1, x2, y2 = re.findall('\d+', l)
        return ((int(x1), int(y1)), (int(x2), int(y2)))
    return [parse_line(l) for l in f]


def day5_1(lines):
    floor = OceanFloor(lines)
    return floor.overlapping_points()


def main():
    with open('input5.txt') as f:
        lines = read_input(f)

    print(f"{day5_1(lines)} overlapping points")


if __name__ == '__main__':
    main()
