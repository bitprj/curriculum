"""
Test Case 4
Note that user input is always after the prompt 'Enter your move (for help enter "H"): '
"""

"""
Description: Testing invalid input and help case - should have no effect on the board - then instant loss
SIZE = 10, MINES = 10, random.seed(5)
"""

"""
Test Case 5 - Results

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
Enter your move (for help enter "H"): 100
Invalid input. Enter your move (for help enter "H"): -100
Invalid input. Enter your move (for help enter "H"): 8f4
Invalid input. Enter your move (for help enter "H"): 4561
Invalid input. Enter your move (for help enter "H"): f43
Invalid input. Enter your move (for help enter "H"): H12
Invalid input. Enter your move (for help enter "H"): H
First, enter the column, followed by the row. To add or remove a flag, add "f" after the row (for example, 64f would place a flag on the 6th column, 4th row). Enter your move: 98F
Invalid input. Enter your move (for help enter "H"): 98f
Mines: 9
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXF 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 64
Mines: 9
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXMXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXF 8
9 XXXXXXXXXX 9
  0123456789
Uh oh! You blew up!
"""
