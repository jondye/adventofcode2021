from pprint import pformat, pprint
import re
from collections import defaultdict


class OceanFloor:
    def __init__(self, lines, include_diagonal=False):
        self.lines = lines
        self.floor = defaultdict(lambda: defaultdict(int))

        def compare(a, b):
            if a > b:
                return 1
            if a < b:
                return -1
            return 0

        for (x, y), (end_x, end_y) in lines:
            x_step = compare(end_x, x)
            y_step = compare(end_y, y)
            if not include_diagonal and (x_step and y_step):
                continue
            steps = max(abs(x - end_x), abs(y - end_y))
            for _ in range(steps + 1):
                self.floor[x][y] += 1
                x += x_step
                y += y_step

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


def day5_2(lines):
    floor = OceanFloor(lines, include_diagonal=True)
    return floor.overlapping_points()


def main():
    with open('input5.txt') as f:
        lines = read_input(f)

    print(f"{day5_1(lines)} overlapping points")
    print(f"{day5_2(lines)} overlapping points including diagonals")


if __name__ == '__main__':
    main()
