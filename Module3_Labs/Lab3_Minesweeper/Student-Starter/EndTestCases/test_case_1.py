"""
Test Case 1
Note that user input is always after the prompt 'Enter your move (for help enter "H"): '
"""

"""
Description: instant loss
SIZE = 10, MINES = 10, random.seed(2)
"""

"""
Test Case 2 - Results
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
Enter your move (for help enter "H"): 42
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXMXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Uh oh! You blew up!
"""
