<!--title={Intro to Graph}-->

The term *graph* can refer to two completely different things. Students usually first learn of a graph as plot of a function, or a function graph. Here, we refer to a different definition of graph, in which a graph is another word for a network.

![Graph](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/1200px-6n-graf.svg.png)

A graph for network is a collection of *nodes* and *edges* that represents relationships:

- **Nodes** are vertices that correspond to objects.
- **Edges** are the connections between objects.
- The graph edges sometimes have **Weights**, which indicate the strength (or some other attribute) of each connection between the nodes

There are two types of graphs:

- A **Directed** graph is made up of a set of vertices connected by edges, where the edges have a direction associated with them. This means you can only move one direction with an edge in a directed graph.
- An **Undirected** graph is made up of a set of vertices connected by edges, where the edges are biderectional, meaning you can go forward or back with an edge in an undirected graph.

Graphs represent networks in real life. They are a good way to imitate networks such as pipeline networks or telephone networks. By imitating these networks, it is easier to simulate how they work and how to solve certain problems that cannot be easily simulated in real life. 

Graphs use two types of data structures: 

- **Adjacency Matrix**:  a 2D array that stores the vertices in the graph. This is used for dense graphs, meaning when the graph has a lot of egdes.

  ![Adjacency Matrix](https://lh3.googleusercontent.com/proxy/iRr8wLaVAVmt8-1V_SM0EOY5udwXiRAcbQFSJEUey6EYaYrhnv4W8LbvIfyFcaX8dGjWP4AEpUzhNFk_RCkZ2BBUJufBBtXy6IvqCRIfCoXsQvIh0LBvhkfLrqS0kAajnee_oPC9eiwet4Ac)

  - Pros:  

    - Representation is easier to implement and follow.
    - Removing an edge takes O(1) time.
    - Looking up an edge takes O(1) time

  - Cons:

    - Takes up more space than an adjacency list
    - Adding a vertex takes O(n^2) time

    

- **Adjacency List**: An array of lists that stores the vertices of the graph.

  ![Adjacency List](https://www.researchgate.net/profile/Carla_Osthoff/publication/274143903/figure/fig3/AS:613978615058433@1523395317311/A-directed-graph-represented-by-adjacency-lists.png)

  - Pros:
    -  Less space compared to Adjacency Matrix
    - Adding a vertex is easier
  - Cons: 
    - Edge look up takes more time (It takes O(n) time as compared to an adjacency matrix that takes O(1) time)

