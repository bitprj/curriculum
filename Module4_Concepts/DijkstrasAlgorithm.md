<!--title={Dijkstra's Algorithm}-->

Dijkstra's algorithm is a single-sourced shortest path algorithm. This means that it is an algorithm used to find the shortest path from node a to another node somwehere in the graph that we can call as node b. It picks the unvisited vertex with the low distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. It was conceived by computer scientist, Edsger W. Dijkstra, in 1956 and published three years later.

```
for each v in V:
	Disc[v]=false
	Dist[v]=infinity
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

- Disc[v] = false when the current vertex has yet to be discovered
- Dist[v]=infinity when the shortest path to vertex v has yet to be calculated
- P[v] = NULL when the parent of the vertex v has yet to be found, meaning that the current vertex v has yet to be discovered
- The above pseudo code only uses lists as the auxillary data structure. However, Dijkstra's can also be implemented via Priority Queues.

- Initially Dist[s] = 0 and all the other Dist[v] values are set to ∞. The algorithm will then process the vertices one by one in some order.

  Here “processing a vertex u” means finding new paths and updating d[v] for all v ∈ Adj[u] if necessary. The process by which an estimate is updated is called **relaxation**.

  When all vertices have been processed,

  Dist[v] = 𝛿 (s,v)  for all v.

  

  ![Dijkstra's](https://i.ytimg.com/vi/pVfj6mxhdMw/hqdefault.jpg)
  
  

Dijkstra's algorithm will assign some initial distance values and will try to improve them step by step.

1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the *unvisited set*.

2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.

3. For the current node, consider all of its unvisited neighbours and calculate their *tentative* distances through the current node. Compare the newly calculated *tentative* distance to the current assigned value and assign the smaller one. For example, if the current node *A* is marked with a distance of 6, and the edge connecting it with a neighbour *B* has length 2, then the distance to *B* through *A* will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.

4. When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the *unvisited set*. A visited node will never be checked again.

5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the *unvisited set* is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.

6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.

    

**Time and Space Complexity**

The Time complexity of the Dijkstra's without using a priority Queue is O(n^2). That is because the first while loop takes O(n) time. The first for loop inside the while loop also takes O(n) time as it does the same thing as the while loop, where it must go through all the vertices in the graph. The second for loop takes O(m) because it checks for the neighbors of the current vertex. Therefore, when you combine them together, you get O(n^2 + m), but since we only care about the highest variable, it is O(n^2).  If a priority queue were to be used, the time complexity would be O(mlgn).

The Space complexity of Dijkstra's with and without the priority queue is O(n). That is because a list is O(n), while a priority queue is O(n) as well in terms of space complexity. 

