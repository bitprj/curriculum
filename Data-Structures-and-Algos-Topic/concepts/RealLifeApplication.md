<!--title={Dijkstra's Algorithm Real Life Application}-->

Suppose that our GPS (Global Positioning System) uses Dijkstra's algorithm to find the shortest route between one location to another, and to demonstrate how this GPS works, let's imagine that graph below is a geographical map—the nodes representing the cities on the map, the edges representing the roads between cities, and the weights of the edges representing distance:

![Dijkstra Algorithm in Java | Baeldung](https://www.baeldung.com/wp-content/uploads/2017/01/initial-graph.png)

For this example, let's try to find the shortest path between the cities A and E. First, we need to keep track of *unvisited cities* and *distances from the starting city* by creating and updating this table:

| NODE: | UNVISITED: | DISTANCE: |
| ----- | ---------- | --------- |
| A*    | False      | 0         |
| B     | True       | ∞         |
| C     | True       | ∞         |
| D     | True       | ∞         |
| E     | True       | ∞         |
| F     | True       | ∞         |

Since we are starting with node A, we will state "False" under the Unvisited column and "0" under the Distance column. The asterisk * next to the node under the Node column indicates which node we are currently at.

Now, we can start using Dijkstra's algorithm!

**Step 1**: Examine the edges leaving A and update the table with the edge's weights under the Distance column. Then, examine this information and pick the edge with the least weight of the unvisited nodes that A reaches—the next node should be B. This is the table should look like now:

| NODE: | UNVISITED: | DISTANCE: |
| ----- | ---------- | --------- |
| A     | False      | 0         |
| B*    | False      | 10        |
| C     | False      | 15        |
| D     | True       | ∞         |
| E     | True       | ∞         |
| F     | True       | ∞         |

**Step 2**: Examine the edges leaving B and update the table again. Look at the Distance column again and select the next node using the same criteria as before—the next node should be D:

| NODE: | UNVISITED: | DISTANCE: |
| ----- | ---------- | --------- |
| A     | False      | 0         |
| B     | False      | 10        |
| C     | False      | 15        |
| D*    | False      | 22        |
| E     | True       | ∞         |
| F     | False      | 25        |

**Step 3**: Examine the edges leaving D and update the table again. Notice that F can be also visited by A through D. If the distance from A to D to F is shorter than the distance from A to B to F, then replace the value under the Distance column for F—in this case, we already reached the end node E, so replacing this value will not be of much use. Here, is what the  table should look like now:

| NODE: | UNVISITED: | DISTANCE: |
| ----- | ---------- | --------- |
| A     | False      | 0         |
| B     | False      | 10        |
| C     | False      | 15        |
| D     | False      | 22        |
| E*    | False      | 24        |
| F     | False      | 25        |

Using Dijkstra's algorithm, we discovered that the shortest path between city A to city E is from A to B to D to E!

---

The space complexity of Dijkstra's algorithm is O(|V|) because we are traversing through the nodes of the graph.

The worst, average, and best case time complexities of Dijkstra's algorithm are O(|E| + |V|log|V|)—E representing the number of edges and V representing the number of vertices/nodes—if a priority queue of distance values is created and we loop through the edges of each node. If a priority queue is not used, then the time complexity would be O(|E| + |V|^2).