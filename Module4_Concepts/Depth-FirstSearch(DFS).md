<!--title={Depth First Search (DFS)}-->

# Depth-First Search 

Depth-First Search(DFS) is one of our data searching algorithms we use in Python to navigate Data structures, Graphs, and Search Trees. DFS is best explained with a visual aide. 

![]( https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Depth-first-tree.svg/450px-Depth-first-tree.svg.png)

DFS starts at a root point and branches on from that point. DFS continues down one path as far as possible before backtracking to the root point and taking an alternate path. 

If we trace the numbers in the visual aide, from 1-12, we get a good sense of idea of how DFS can navigates data and graphs. 

1. Choose one route and continue down that route until a dead end is reached. 

   Circle 1 -> to Circle 2 -> to Circle 3 -> Circle 4

2. Once a dead end is reached, we backtrack to previous nodes until we find another path not yet explored. 

   Circle 4 -> to Circle 3 

3. We continue down that new path. 

   Circle 3 -> Circle 5 

4. Then, we backtrack to the next available path. 

   Circle 5 -> Circle 3 -> Circle 2

5. Circle 2 has the available path of Circle 6.

6. We continue this pattern until we have searched the entire data structure, tree, or graph. 

To explain it in terms of python, we follow these rules.

- **Rule 1** − Visit the adjacent unvisited vertex. Mark it as visited. Display it. Push it in a stack.
- **Rule 2** − If no adjacent vertex is found, pop up a vertex from the stack. (It will pop up all the vertices from the stack, which do not have adjacent vertices.)
- **Rule 3** − Repeat Rule 1 and Rule 2 until the stack is empty.

### DFS in Python

```Python
# Python3 program to print DFS traversal 
# from a given given graph 
from collections import defaultdict 

# This class represents a directed graph using 
# adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	# function to add an edge to graph 
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	# A function used by DFS 
	def DFSUtil(self, v, visited): 

		# Mark the current node as visited 
		# and print it 
		visited[v] = True
		print(v, end = ' ') 

		# Recur for all the vertices 
		# adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 

	# The function to do DFS traversal. It uses 
	# recursive DFSUtil() 
	def DFS(self, v): 

		# Mark all the vertices as not visited 
		visited = [False] * (len(self.graph)) 

		# Call the recursive helper function 
		# to print DFS traversal 
		self.DFSUtil(v, visited) 

# Driver code 

# Create a graph given 
# in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print("Following is DFS from (starting from vertex 2)") 
g.DFS(2) 

# This code is contributed by Neelam Yadav 
```

---

The time complexity of DFS is O(N^M), if N is the number of nodes in a tree and M is the maximum depth of the tree.

The space complexity of DFS is O(NM) because we have N nodes at the maximum depth M and (N-1) nodes at earlier depths (M-1). To find the space used, we find the total, which would be N + (M-1)*(N-1) = NM.