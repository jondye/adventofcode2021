with open('input2.txt') as f:
    instructions = [x.split() for x in f.readlines()]

position = {"h": 0, "v": 0}
for cmd, amount in instructions:
    if cmd == "forward":
        position['h'] += int(amount)
    elif cmd == "down":
        position['v'] += int(amount)
    elif cmd == "up":
        position['v'] -= int(amount)

print(position)
print(position['h'] * position['v'])