import random

from checkpoint1 import create_board


def test_case1(size, mines):
    board = create_board(size, mines)
    print(board)


def test_case2(size, mines):
    # for keeping board consistent
    random.seed(5)
    board = create_board(size, mines)
    board.show(2, 3)
    board.flag(4, 6)
    print(board)


def test_case3(size, mines):
    # for keeping board consistent
    random.seed(9)
    board = create_board(size, mines)
    board.show(3, 7)
    board.flag(0, 0)
    print(board)


def test_case4(size, mines):
    # for keeping board consistent
    random.seed(9)
    board = create_board(size, mines)
    board.show(3, 7)
    board.flag(0, 0)
    board.show(4, 0)
    board.show(6, 2)
    board.show(7, 2)

    print(board)


def test_case5(size, mines):
    # for keeping board consistent
    random.seed(9)
    board = create_board(size, mines)
    board.show(3, 7)
    board.flag(0, 0)
    board.show(4, 0)
    board.show(6, 2)
    board.show(7, 2)
    board.flag(7, 0)
    board.show(4, 2)
    board.show(8, 4)
    board.show(8, 0)
    print(board)


def main():
    test_case1(7, 9)
    test_case2(7, 9)
    test_case3(9, 10)
    test_case4(9, 10)
    test_case5(9, 10)

main()