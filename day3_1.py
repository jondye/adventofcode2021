with open('input3.txt') as f:
    lines = [n.strip() for n in f.readlines()]

# Turn binary strings (0010001) into lists of numbers ([0, 0, 1, 0, 0, 0, 1])
numbers = ([int(x) for x in l] for l in lines)

# sum the columns (to count the ones)
sums = [sum(x) for x in zip(*numbers)]

# calculate gamma
half = len(lines) / 2
gamma_string = "".join('1' if ones > half else '0' for ones in sums)
gamma = int(gamma_string, 2)

# calculate epsilon
epsilon_string = "".join('1' if ones < half else '0' for ones in sums)
epsilon = int(epsilon_string, 2)

power = epsilon * gamma
print(f"gamma={gamma}\nepsilon={epsilon}\npower={power}")