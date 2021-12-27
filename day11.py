import numpy as np

def day11_1(octopuses):
    return None

def increase(octopuses, x, y):
    if 0 <= x < octopuses.shape[0] and 0 <= y < octopuses.shape[1]:
        octopuses[x,y] += 1
        if octopuses[x,y] == 10:
            increase(octopuses, x-1, y-1)
            increase(octopuses, x, y-1)
            increase(octopuses, x+1, y-1)

            increase(octopuses, x-1, y)
            increase(octopuses, x+1, y)

            increase(octopuses, x-1, y+1)
            increase(octopuses, x, y+1)
            increase(octopuses, x+1, y+1)
    return octopuses

def step(octopuses):
    for y in range(octopuses.shape[1]):
        for x in range(octopuses.shape[1]):
            increase(octopuses, x, y)
    return octopuses

def main():
    with open('input11.txt') as f:
        octopuses = np.array([[int(x) for x in l.strip()] for l in f.readlines()])
    print(f"After 100 rounds there were {day11_1(octopuses)} flashes")

if __name__ == '__main__':
    main()