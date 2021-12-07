class Fish:
    def __init__(self, state):
        self.state = state

    def time_passes(self, days):
        for _ in range(days):
            new_fish = [8 for fish in self.state if fish == 0]
            self.state = [(fish - 1) if fish > 0 else 6 for fish in self.state]
            self.state += new_fish

    def count(self):
        return len(self.state)

def main():
    with open('input6.txt') as f:
        state = [int(fish) for fish in f.readline().split(',')]

    f = Fish(state)
    f.time_passes(80)
    print(f"There are {f.count()} fish after 80 days")

if __name__ == '__main__':
    main()