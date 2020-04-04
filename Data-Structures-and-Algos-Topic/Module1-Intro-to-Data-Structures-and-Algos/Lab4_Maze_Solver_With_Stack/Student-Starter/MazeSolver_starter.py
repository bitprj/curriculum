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
    pass


def loadFile(fileName):  # load grid from file and return as pointer to
    return 'TO-DO'


# pointer to grid as parameter
def printGrid(grid):
    return 'TO-DO'


def gotoxy(x, y):  # function to show cursor position on screen
    return 'TO-DO'


def inArray(rowCheck, columnCheck, arrSize, r, c):  # check if a point on
    return 'TO-DO'


def solveMaze(maze):
    return 'TO-DO'


def main():
    return 0


main()