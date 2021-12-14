from collections import Counter


def day10_1(lines):
    missmatches = [first_missmatch(l) for l in lines]
    counts = Counter(missmatches)
    return sum(
        counts[c] * score
        for c, score in [(")", 3), ("]", 57), ("}", 1197), (">", 25137)])


def first_missmatch(line):
    stack = []
    for c in line:
        try:
            stack.append(']}>)'['[{<('.index(c)])
        except ValueError:
            if c != stack.pop():
                return c


def main():
    with open('input10.txt') as f:
        lines = [l.strip() for l in f.readlines()]
    print(f"syntax score: {day10_1(lines)}")


if __name__ == '__main__':
    main()
