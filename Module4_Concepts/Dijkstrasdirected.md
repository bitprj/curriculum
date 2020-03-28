<!--title={Dijkstra's Algorithm Directed graph}-->

Dijkstra's Algorithm solves one of the more common questions in computer science: the shortest path from location a to location b. Dijskstra's algorithm works specifically on graphs, both directed and undirected. Here is the pseudo code for the algorithm:

```
init lists Disc, Dist, and P, each of lenght |V|
for each v in V:
	Disc[v]=false
	Disc[v]=infinity
	P[v]=NULL
Dist[s]=0
P[s]=None
Num_Discovered = 0
while Num_Discovered < |V|:
	min_dist = infinity
	min_v = NULL
	for each v in V:
		if Disc[v] = false and Dist[v] < min_dist:
			min_dist = Dist[v]
			min_v = v
  Disc[v] = true
  Num_Discovered = Num_Discovered + 1
  for each neighbor n of v: 
  	if Dist[v] + cost(v, n) < Dist[n]:
    	Dist[n] = Dist[v] + cost(v, n)
    	P[n] = v

```

The while loop takes O(n) time because it goes through all the vertices in the graph. The first for loop takes O(n) time as well as it also has to go through all the vertices in the graph as well. The second for loop, on the other hand, takes O(m) time because it checks for the neighbors of each vertex inside the graph. Therefore, when you add all of that together, you get a time complexity of O(n^2 + m), which can be simplified to O(n^2) since we only care about the biggest variable when talking about time complexity. 

The space complexity of the algorithm, on the other hand, is only O(n) that is because of the various lists used to find the shortest path from location a to location b. Even though there are three lists, making the space complexity O(3n), we usually don't care about the constant. Therefore, it is O(n). 

An important thing to take note of is that Dijsktra's Algorithm does not discriminate between directed and undirected graphs. That is because it works for both, the only difference being what is inside the adjacency list or adjacency matrix that is used to implement the graph. Therefore, the above pseudo code will work on both directed and and undirected graphs.

Here is an example of a directed graph with Dijsktra's algorithm being used on it:

<img src="/Users/jr194/Bit Prjct/curriculum/Module4_Concepts/Example_1.png" style="zoom:40%;" />

