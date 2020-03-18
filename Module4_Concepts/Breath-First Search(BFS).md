<!--title={Breath First Search (BFS)}-->

# Breath-First Search

Breath-First Search(BFS) is one of our data searching algorithms we can use to navigate data, graphs, or search trees. BFS is best explained using a visual aide. 

![]( https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Breadth-first-tree.svg/1200px-Breadth-first-tree.svg.png )

The number of each circle is the order in which we navigate our data structure. Let's examine how and why we take the path we do. 

1. We originally start at a **root** point. In our visual aide, our  start would be 1. 
2. We notice that there are 3 branches attached to Circle 1. These branches are circles 2, 3, and 4. 
3. At circle 2 and circle 4, we notice that each have two nodes branching from them. Circle's 5 and 6 are attached to circle 2, and Circle's 7 and 8 are attached to Circle 4. Circle 3 has no nodes attached to it, so we know we no longer  need to explore the "Circle 3 path". 
4. We explore all the paths attached to Circle 2 and Circle 4. In BFS, we are, at max, one node deep at a time. For example, after exploring Circle 5, we note that two nodes are available, Circle 9 and Circle 10, but we do not explore these circles. After exploring Circle 5, we turn back to Circle 2 and then proceed to explore Circle 6.
5. We repeat this process for Circles 6, 7, and 8 noting any attached nodes. We notice that Circle 6 and 7 have no nodes attached to them so we no longer need to go down those paths.
6. Repeat this process until we've completely explored the entire map. 

## BFS in Python

Below is a python function that incorporates BFS.

```python
# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# Function to print a BFS of graph 
	def BFS(self, s): 

		# Mark all the vertices as not visited 
		visited = [False] * (len(self.graph)) 

		# Create a queue for BFS 
		queue = [] 

		# Mark the source node as 
		# visited and enqueue it 
		queue.append(s) 
		visited[s] = True

		while queue: 

			# Dequeue a vertex from 
			# queue and print it 
			s = queue.pop(0) 
			print (s, end = " ") 

			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then mark it 
			# visited and enqueue it 
			for i in self.graph[s]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True

# Driver code 

# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
g.BFS(2) 

# This code is contributed by Neelam Yadav 
```

The Big O time and space complexity is O(|V+E|). |V| symbolizes all the vertices in the tree. |E| symbolizes all the edges in the tree. Since you need to traverse them all at worst case, Big O is a function of all the vertices. 
