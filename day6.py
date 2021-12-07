from collections import Counter
class Fish:
    def __init__(self, state):
        self.state = Counter(state)

    def time_passes(self, days):
        for _ in range(days):
            new_fish = self.state[0]
            for age in range(0, 8):
                self.state[age] = self.state[age + 1]
            self.state[6] += new_fish
            self.state[8] = new_fish

    def count(self):
        return self.state.total()

def main():
    with open('input6.txt') as f:
        state = [int(fish) for fish in f.readline().split(',')]

    f = Fish(state)
    f.time_passes(80)
    print(f"There are {f.count()} fish after 80 days")
    f.time_passes(256 - 80)
    print(f"There are {f.count()} fish after 256 days")

if __name__ == '__main__':
    main()