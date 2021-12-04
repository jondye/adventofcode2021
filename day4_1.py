from pprint import pformat

class Board:
    def __init__(self, rows):
        self.rows = rows

    def bingo(self):
        return (any(all(item is None for item in row) for row in self.rows) or
                any(all(item is None for item in column) for column in self.columns))

    def call(self, number):
        self.rows = [[None if item == number else item for item in row]
                     for row in self.rows]

    def unmarked_sum(self):
        return sum(item for row in self.rows for item in row if item is not None)

    @property
    def columns(self):
        return list(list(column) for column in zip(*self.rows))

    def __repr__(self):
        return pformat(self.rows)


def main():
    boards = []
    calls = []
    with open('input4.txt') as f:
        calls = [int(x) for x in f.readline().strip().split(',')]
        
        while f.readline():
            rows = []
            for row in range(5):
                rows.append([int(x) for x in f.readline().strip().split()])
            boards.append(Board(rows))

    for c in calls:
        for index, board in enumerate(boards):
            board.call(c)
            if board.bingo():
                print(f"Bingo (board {index+1})")
                print(board.unmarked_sum() * c)
                return



if __name__ == '__main__':
    main()
