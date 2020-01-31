
"""
Test Case 1
def main():
    SIZE = 7
    MINES = 9
    board = create_board(SIZE, MINES)
    print(board)

"""
"""
Test Case 1 - Results
Mines: 9
  0123456
0 XXXXXXX 0
1 XXXXXXX 1
2 XXXXXXX 2
3 XXXXXXX 3
4 XXXXXXX 4
5 XXXXXXX 5
6 XXXXXXX 6
  0123456
  """


"""
Test Case 2

def main():
    SIZE = 7
    MINES = 9
    # for keeping board consistent
    random.seed(5)
    board = create_board(SIZE, MINES)
    board.show(2, 3)
    board.flag(4, 6)
    print(board)
"""

"""
Test Case 2 - Results
Mines: 8
  0123456
0 XXXXXXX 0
1 XXXXXXX 1
2 XXXMXXX 2
3 XXXXXXX 3
4 XXXXXXF 4
5 XXXXXXX 5
6 XXXXXXX 6
  0123456

"""


"""
Test Case 3

def main():
    SIZE = 9
    MINES = 10
    # for keeping board consistent
    random.seed(9)
    board = create_board(SIZE, MINES)
    board.show(3, 7)
    board.flag(0, 0)
    print(board)

"""


"""
Test Case 3 - Results

Mines: 9
  012345678
0 F1        0
1 X1        1
2 X111221   2
3 XXXXXX1   3
4 XXXXXX21  4
5 XXXXXXX1  5
6 XXXXXXX2  6
7 XXXXXXX1  7
8 XXXXXXX1  8
  012345678

"""

"""
Test Case 4
def main():
    SIZE = 9
    MINES = 10
    # for keeping board consistent
    random.seed(9)
    board = create_board(SIZE, MINES)
    board.show(3, 7)
    board.flag(0, 0)
    board.show(4, 0)
    board.show(6, 2)
    board.show(7, 2)

    print(board)

"""

"""
Test Case 4 - Results

Mines: 9
  012345678
0 F1        0
1 X1        1
2 X111221   2
3 XXXXXX1   3
4 1XXXXX21  4
5 XXXXXXX1  5
6 XX1XXXX2  6
7 XX2XXXX1  7
8 XXXXXXX1  8
  012345678

"""

"""
Test Case 5
def main():
    SIZE = 9
    MINES = 10
    # for keeping board consistent
    random.seed(9)
    board = create_board(SIZE, MINES)
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
"""

"""
Test Case 5 - Results

Mines: 8
  012345678
0 F1        0
1 X1        1
2 X111221   2
3 XXXXXX1   3
4 1X222321  4
5 XXX1 1X1  5
6 XX11 2X2  6
7 FX21 1X1  7
8 MXX1 1X1  8
  012345678

"""
