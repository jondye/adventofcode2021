from itertools import pairwise

def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c

with open('input1.txt') as f:
    depths = [int(x) for x in f.readlines()]
m3 = triplewise(depths)
print(sum(sum(y) > sum(x) for x, y in pairwise(m3)))