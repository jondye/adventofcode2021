from collections import Counter


def day10_1(lines):
    mismatches = [syntax_check(l)[0] for l in lines]
    counts = Counter(mismatches)
    return sum(
        counts[c] * score
        for c, score in [(")", 3), ("]", 57), ("}", 1197), (">", 25137)])


def day10_2(lines):
    missing = (syntax_check(l)[1] for l in lines)
    scores = sorted(score(m) for m in missing if m)
    return scores[len(scores) // 2]


def syntax_check(line):
    stack = []
    for c in line:
        try:
            stack.append(']}>)'['[{<('.index(c)])
        except ValueError:
            if c != stack.pop():
                return c, None
    return None, "".join(reversed(stack))


def score(missing):
    total = 0
    for c in missing:
        points = ")]}>".index(c) + 1
        total = 5 * total + points
    return total


def main():
    with open('input10.txt') as f:
        lines = [l.strip() for l in f.readlines()]
    print(f"syntax score: {day10_1(lines)}")
    print(f"middle completion score: {day10_2(lines)}")


if __name__ == '__main__':
    main()
