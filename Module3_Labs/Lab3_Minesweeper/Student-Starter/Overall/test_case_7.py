"""
Test Case 7
Note that user input is always after the prompt 'Enter your move (for help enter "H"): '
"""

"""
Description: Showing and flagging cells en route to a victory.
SIZE = 10, MINES = 10, random.seed(6)

"""
"""
Test Case 7 - Results

Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 34
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXX2XXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 63
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXX1XXX 3
4 XXX2XXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 78
Mines: 10
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XX1    4
5  1XXXX21   5
6  13XXXX1   6
7   2X2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 37f
Mines: 9
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XX1    4
5  1XXXX21   5
6  13XXXX1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 36f
Mines: 8
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XX1    4
5  1XXXX21   5
6  13FXXX1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 46
Mines: 8
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XX1    4
5  1XXXX21   5
6  13F2XX1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 56
Mines: 8
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XX1    4
5  1XXXX21   5
6  13F21X1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 66f
Mines: 7
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XX1    4
5  1XXXX21   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 54f
Mines: 6
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XF1    4
5  1XXXX21   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 55
Mines: 6
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XF1    4
5  1XXX221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 53
Mines: 6
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XF1    4
5  1XXX221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 54
Mines: 6
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XF1    4
5  1XXX221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 35
Mines: 6
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XF1    4
5  1X2X221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 45
Mines: 6
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X2XF1    4
5  1X22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 44
Mines: 6
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X22F1    4
5  1X22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 25f
Mines: 5
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 11XXX21    3
4  1X22F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 23
Mines: 5
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 111XX21    3
4  1X22F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 24
Mines: 5
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 111XX21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 33
Mines: 5
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 1111X21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 43f
Mines: 4
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XXXXX1     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 22
Mines: 4
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XX1XX1     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 32
Mines: 4
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XX11X1     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 42
Mines: 4
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XX1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 12f
Mines: 3
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 XF1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 02
Mines: 3
  0123456789
0 XXXXX1     0
1 XXXXX1     1
2 2F1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 11
Mines: 3
  0123456789
0 XXXXX1     0
1 X3XXX1     1
2 2F1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 21
Mines: 3
  0123456789
0 XXXXX1     0
1 X31XX1     1
2 2F1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 31
Mines: 3
  0123456789
0 XXXXX1     0
1 X311X1     1
2 2F1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 10
Mines: 3
  0123456789
0 X2XXX1     0
1 X311X1     1
2 2F1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 20
Mines: 3
  0123456789
0 X2 1X1     0
1 X311X1     1
2 2F1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 30
Mines: 3
  0123456789
0 X2 1X1     0
1 X311X1     1
2 2F1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 41
Mines: 3
  0123456789
0 X2 1X1     0
1 X31111     1
2 2F1111     2
3 1111F21    3
4  1122F1    4
5  1F22221   5
6  13F21F1   6
7   2F2111   7
8   111      8
9            9
  0123456789
Well done! You solved the board!
"""
