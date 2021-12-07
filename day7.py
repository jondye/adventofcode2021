class Crabs:
    def __init__(self, positions):
        self.positions = positions
        self.max_position = max(self.positions)
        self.costs = TriangularNumbers()

    def best_position(self, cost_function):
        _, position = min(
            (sum(cost_function(position)), position)
            for position in range(self.max_position + 1))
        return position

    def best_position_by_distance(self):
        return self.best_position(self.distance_from)

    def best_position_by_fuel(self):
        return self.best_position(self.fuel_costs_to)

    def distance_from(self, position):
        return [abs(position - x) for x in self.positions]

    def fuel_costs_to(self, position):
        distances = self.distance_from(position)
        return [self.costs[x] for x in distances]


class TriangularNumbers:
    def __init__(self):
        self.numbers = [0]

    def __getitem__(self, index):
        for i in range(len(self.numbers), index + 1):
            self.numbers.append(self.numbers[-1] + i)
        return self.numbers[index]


def day7_1(positions):
    c = Crabs(positions)
    position = c.best_position_by_distance()
    return sum(c.distance_from(position))


def day7_2(positions):
    c = Crabs(positions)
    position = c.best_position_by_fuel()
    return sum(c.fuel_costs_to(position))


def main():
    with open('input7.txt') as f:
        positions = [int(x) for x in f.readline().strip().split(',')]
    print(f"Minimum fuel used with linear consumption is {day7_1(positions)}")
    print(f"Minimum fuel used with is {day7_2(positions)}")


if __name__ == '__main__':
    main()
