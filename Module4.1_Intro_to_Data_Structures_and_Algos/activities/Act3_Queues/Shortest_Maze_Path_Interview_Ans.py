# Credit to https://www.techiedelight.com/lee-algorithm-shortest-path-in-a-maze/ for solution and problem.

# import the deque library
from collections import deque


# queue node used in BFS
class Node:
	# (x, y) represents matrix cell coordinates
	# dist represents its minimum distance from the source
	def __init__(self, x, y, dist):
		x = self.x
		y = self.y
		dist = self.dist


# Function to check if it is possible to go to position (row, col)
# from current position. The function returns false if (row, col)
# is not a valid position or has value 0 or it is already visited
def isValid(mat, visited, row, col):
	return ((row >= 0) and (row < M) and (col >= 0) and (col < N) and (mat[row][col]) and (not visited[row][col]))    	


# Find Shortest Possible Route in a matrix mat from source
# cell (i, j) to destination cell (x, y)
def BFS(mat, i, j, x, y):
	# // construct a matrix to keep track of visited cells
	# see https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/ for more details on how to initialize a 2D list in Python
	visited = [[0] * N] * M

	# create an empty queue
	q = deque()

	# mark source cell as visited and enqueue the source node
	visited[i][j] = True
	q.append(Node(i, j, 0))

	# stores length of longest path from source to destination
	min_dist = sys.maxsize

	# run till queue is not empty
	while (not q.empty()):




def main():
	# M x N matrix
	M = 10;
	N = 10;

	# Below arrays details all 4 possible movements from a cell
	row = {-1, 0, 0, 1}
	col = {0, -1, 1, 0}






		


