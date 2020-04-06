# Credit to https://www.techiedelight.com/lee-algorithm-shortest-path-in-a-maze/

# import the deque library
from collections import deque
import sys

# Global variables
# M x N matrix
M = 10;
N = 10;

# Below arrays details all 4 possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

# queue node used in BFS
class Node:
	# (x, y) represents matrix cell coordinates
	# dist represents its minimum distance from the source
	def __init__(self, x, y, dist):
		self.x = x
		self.y = y
		self.dist = dist


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
	# make sure to read above article to all the way to the end. it is possible a reader may be confused and get unanticipated
	# results with their 2D list initialization if they do not read all the way to the end
	# note that visited = [[False] * N] * M] does NOT work as intended (see article for more details)
	visited = [[False for n in range(N)] for m in range(M)]

	# create an empty queue
	q = deque()

	# mark source cell as visited and enqueue the source node
	visited[i][j] = True
	q.append(Node(i, j, 0))

	# stores length of longest path from source to destination
	min_dist = sys.maxsize

	# run till queue is not empty
	while q:
		# pop front (left) node from queue and process it
		node = q.popleft()

		# (i, j) represents current cell and dist stores its
	    # minimum distance from the source
		i = node.x
		j = node.y
		dist = node.dist


	    # if destination is found, update min_dist and stop
		if i == x and j == y:
			min_dist = dist
			break

	    # check for all 4 possible movements from current cell
	    # and enqueue each valid movement
		for k in range(4):
	    	# check if it is possible to go to position
	        # (i + row[k], j + col[k]) from current position
		    if (isValid(mat, visited, i + row[k], j + col[k])):
		    	visited[i + row[k]][j + col[k]] = True
		    	q.append(Node(i + row[k], j + col[k], dist + 1))

	if min_dist != sys.maxsize:
		print("The shortest path from source to destination has length", min_dist)
	else:
		print("destination can't be reached from given source")	        	

# Shortest path in a Maze
def main():

	# input maze of size M x N
	mat = [
    	[ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
        [ 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 ],
        [ 0, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
        [ 1, 0, 1, 1, 1, 0, 1, 1, 0, 1 ],
        [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 1 ],
        [ 1, 0, 1, 1, 1, 0, 0, 1, 1, 0 ],
        [ 0, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
        [ 0, 1, 1, 1, 1, 1, 1, 1, 0, 0 ],
        [ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
        [ 0, 0, 1, 0, 0, 1, 1, 0, 0, 1 ],
  		]

  	# Find shortest path from source (0, 0) to
    # destination (7, 5)
	BFS(mat, 0, 0, 7, 5)


main()





		


