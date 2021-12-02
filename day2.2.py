with open('input2.txt') as f:
    instructions = [x.split() for x in f.readlines()]

position = {"pos": 0, "depth": 0, "aim": 0}
for cmd, amount in instructions:
    if cmd == "forward":
        position['depth'] += int(amount)
        position['pos'] += position['aim'] * int(amount)
    elif cmd == "down":
        position['aim'] += int(amount)
    elif cmd == "up":
        position['aim'] -= int(amount)

print(position)
print(position['depth'] * position['pos'])