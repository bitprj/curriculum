<!--title={Dijkstra's Algorithm Undirected graph}-->

Now, let's apply the algorithm to an undirected graph!

[![Fig-1](https://www.geeksforgeeks.org/wp-content/uploads/Fig-11.jpg)](https://www.geeksforgeeks.org/wp-content/uploads/Fig-11.jpg)

The set *sptSet* is initially empty and distances assigned to vertices are {0, INF, INF, INF, INF, INF, INF, INF} where INF indicates infinite. Now pick the vertex with minimum distance value. The vertex 0 is picked, include it in *sptSet*. So *sptSet* becomes {0}. After including 0 to *sptSet*, update distance values of its adjacent vertices. Adjacent vertices of 0 are 1 and 7. The distance values of 1 and 7 are updated as 4 and 8. Following subgraph shows vertices and their distance values, only the vertices with finite distance values are shown. The vertices included in SPT are shown in green colour.

[![Fig-2](https://www.geeksforgeeks.org/wp-content/uploads/MST1.jpg)](https://www.geeksforgeeks.org/wp-content/uploads/MST1.jpg)

Pick the vertex with minimum distance value and not already included in SPT (not in sptSET). The vertex 1 is picked and added to sptSet. So sptSet now becomes {0, 1}. Update the distance values of adjacent vertices of 1. The distance value of vertex 2 becomes 12.

[![Fig-3](https://www.geeksforgeeks.org/wp-content/uploads/DIJ2.jpg)](https://www.geeksforgeeks.org/wp-content/uploads/DIJ2.jpg)

Pick the vertex with minimum distance value and not already included in SPT (not in sptSET). Vertex 7 is picked. So sptSet now becomes {0, 1, 7}. Update the distance values of adjacent vertices of 7. The distance value of vertex 6 and 8 becomes finite (15 and 9 respectively).
[![Fig-4](https://www.geeksforgeeks.org/wp-content/uploads/DIJ3.jpg)](https://www.geeksforgeeks.org/wp-content/uploads/DIJ3.jpg)

Pick the vertex with minimum distance value and not already included in SPT (not in sptSET). Vertex 6 is picked. So sptSet now becomes {0, 1, 7, 6}. Update the distance values of adjacent vertices of 6. The distance value of vertex 5 and 8 are updated.

[![Fig-4](https://www.geeksforgeeks.org/wp-content/uploads/DIJ4.jpg)](https://www.geeksforgeeks.org/wp-content/uploads/DIJ4.jpg)

We repeat the above steps until *sptSet* does include all vertices of given graph. Finally, we get the following Shortest Path Tree (SPT).

[![Fig-1](https://www.geeksforgeeks.org/wp-content/uploads/DIJ5.jpg)](https://www.geeksforgeeks.org/wp-content/uploads/DIJ5.jpg)

---

Keep in mind that Dijkstra's algorithm can also be used on directed graphs as well! In regard to directed graphs, be sure to pay attention to the direction of the edges and realize that the shortest path that you looking for cannot go against the direction of the edges it consists of.