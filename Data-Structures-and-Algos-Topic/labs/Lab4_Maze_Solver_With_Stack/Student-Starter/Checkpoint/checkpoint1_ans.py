ROWS = 30
COLUMNS = 100
import time
import os
from ctypes import *

STD_OUTPUT_HANDLE = -11


class COORD(Structure):
    pass


COORD._fields_ = [("X", c_short), ("Y", c_short)]


class Stack:
    def __init__(self):
        self.index = -1
        self.arr = [None] * ROWS * COLUMNS

    # add new value to top of stack
    def push(self, a):
        self.index = self.index + 1
        self.arr[self.index] = a

    # return value at top of stack and set index to value below
    def pop(self):
        self.index = self.index - 1
        return self.arr[self.index + 1]

    # return value at top of stack
    def top(self):
        return self.arr[self.index]

    # check if stack is full or empty
    def isFull(self):
        return ((self.index + 1) == ROWS * COLUMNS if True else False)

    def isEmpty(self):
        return (self.index == 0 if True else False)


def loadFile(fileName):  # load grid from file and return as pointer to 2D array
    with open(fileName, 'r') as file:
        data = file.readlines()

    # initialize 2D grid array
    w, h = COLUMNS, ROWS
    grid = [[0 for x in range(w)] for y in range(h)]
    # write content of file into grid
    i = 0
    j = 0
    for line in data:
        j = 0
        for word in line:

            grid[i][j] = word
            # blank if '0'
            if grid[i][j] == '0':
                grid[i][j] = 32
            # wall if '1'
            elif (grid[i][j] == '1'):
                grid[i][j] = 9608
            # door (dotted wall) if '3'
            elif (grid[i][j] == '3'):
                grid[i][j] = 9618
            j = j + 1
            if j == COLUMNS:
                break
        i = i + 1
        if i == ROWS:
            break
    file.close()
    return grid


# pointer to grid as parameter
def printGrid(grid):
    os.system("color 3")  # set color of grid
    # print grid
    for r in range(0, ROWS):
        for c in range(0, COLUMNS):
            print(chr(grid[r][c]), end="")
        print(" ")
        
# NOT NEEDED IN THIS CHECKPOINT

"""
def gotoxy(x, y):  # function to show cursor position on screen
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(x, y))


def inArray(rowCheck, columnCheck, arrSize, r, c):  # check if a point on grid is already visited
    for i in range(0, arrSize):
        if (rowCheck[i] == r and columnCheck[i] == c):
            return True
    return False


def solveMaze(maze):
    r = 1
    c = 0
    # starting position of maze
    maze[1][-1] = -37
    rowStack = Stack()
    columnStack = Stack()
    rowVisited = [None] * ROWS * COLUMNS
    colVisited = [None] * ROWS * COLUMNS
    visitedPointsIndex = 0
    gotoxy(c, r)
    print("X")

    while maze[r][c] != 9618:  # loop until exit found
        gotoxy(c, r)
        print(" ")
        #
        #       if statements check:
        #	    1) if the point is blank
        #	    2) if the point was not most previously visited and
        #	    3) if the path of the point did not already lead to a dead-end
        #
        # check up
        if ((maze[r - 1][c] == 32 or maze[r - 1][c] == 9618)
                and ((r - 1) != rowStack.top())
                and not inArray(rowVisited, colVisited, ROWS * COLUMNS, r - 1, c)):
            rowStack.push(r)
            r = r - 1
            columnStack.push(c)
        # check down
        elif ((maze[r + 1][c] == 32 or maze[r + 1][c] == 9618)
              and ((r + 1) != rowStack.top())
              and not inArray(rowVisited, colVisited, ROWS * COLUMNS, r + 1, c)):
            rowStack.push(r)  # add r value to stack and increment r to move down
            r = r + 1
            columnStack.push(c)  # add c value to stack
        # check left
        elif ((maze[r][c - 1] == 32 or maze[r][c - 1] == 9618)
              and ((c - 1) != columnStack.top())
              and not inArray(rowVisited, colVisited, ROWS * COLUMNS, r, c - 1)):
            rowStack.push(r)
            columnStack.push(c)
            c = c - 1
        # check right
        elif ((maze[r][c + 1] == 32 or maze[r][c + 1] == 9618)
              and ((c + 1) != columnStack.top())
              and not inArray(rowVisited, colVisited, ROWS * COLUMNS, r, c + 1)):
            rowStack.push(r)
            columnStack.push(c)
            c = c + 1
        # if no blank field not previously visited available
        else:
            if (not rowStack.isEmpty()):
                # add present point to arrays of already visited points that led to a dead-end
                rowVisited[visitedPointsIndex] = r
                colVisited[visitedPointsIndex] = c
                visitedPointsIndex = visitedPointsIndex + 1
                # change point to last visited point
                r = rowStack.pop()
                c = columnStack.pop()

        # move cursor on screen
        gotoxy(c, r)
        print("X")
        # delay to see change
        #time.sleep(0.05)
"""

def main():
    # load maze and another grid to display after exit found
    mazeFile = "maze.txt"
    doneFile = "done.txt"
    maze = loadFile(mazeFile)
    done = loadFile(doneFile)
    # print and solve maze
    printGrid(maze)
    #NOT NEEDED IN THIS CHECKPOINT
    """
      #solveMaze(maze)

    # print grid to show maze completed
    printGrid(done)
    time.sleep(20)
    """
  
    return 0


main()