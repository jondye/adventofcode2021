from day4 import *

board_1 = [
    [22, 13, 17, 11,  0],
    [8,  2, 23,  4, 24],
    [21,  9, 14, 16,  7],
    [6, 10,  3, 18,  5],
    [1, 12, 20, 15, 19]]

board_2 = [
    [3, 15,  0,  2, 22],
    [9, 18, 13, 17,  5],
    [19,  8,  7, 25, 23],
    [20, 11, 10, 24,  4],
    [14, 21, 16, 12,  6]]

board_3 = [
    [14, 21, 17, 24,  4],
    [10, 16, 15,  9, 19],
    [18,  8, 23, 26, 20],
    [22, 11, 13,  6,  5],
    [2,  0, 12,  3,  7]]


def test_row_bingo():
    board = Board(board_3)
    assert not board.bingo()
    board.call(7)
    assert not board.bingo()
    board.call(4)
    assert not board.bingo()
    board.call(9)
    assert not board.bingo()
    board.call(5)
    assert not board.bingo()
    board.call(11)
    assert not board.bingo()
    board.call(17)
    assert not board.bingo()
    board.call(23)
    assert not board.bingo()
    board.call(2)
    assert not board.bingo()
    board.call(0)
    assert not board.bingo()
    board.call(14)
    assert not board.bingo()
    board.call(21)
    assert not board.bingo()
    board.call(24)
    assert board.bingo()
    assert board.unmarked_sum() == 188


def test_column_bingo():
    board = Board(board_3)
    assert not board.bingo()
    board.call(14)
    assert not board.bingo()
    board.call(10)
    assert not board.bingo()
    board.call(18)
    assert not board.bingo()
    board.call(2)
    assert not board.bingo()
    board.call(22)
    assert board.bingo()
    #assert board.unmarked_sum() == 259


def test_board_rows():
    board = Board(board_3)
    assert board.rows[0] == [14, 21, 17, 24, 4]
    assert board.rows[1] == [10, 16, 15,  9, 19]
    assert board.rows[2] == [18,  8, 23, 26, 20]
    assert board.rows[3] == [22, 11, 13,  6,  5]
    assert board.rows[4] == [2,  0, 12,  3,  7]


def test_board_columns():
    board = Board(board_3)
    assert board.columns[0] == [14, 10, 18, 22, 2]


def test_day4_2():
    boards = [Board(board_1), Board(board_2), Board(board_3)]
    calls = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
             16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    last_call, last_board = day4_2(calls, boards)
    assert last_call == 13
    assert last_board == boards[1]
