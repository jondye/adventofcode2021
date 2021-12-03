with open('input1.txt') as f:
    depths = [int(x) for x in f.readlines()]
print(sum(y>x for x, y in zip(depths, depths[1:])))