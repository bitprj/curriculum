# Find the Shortest Path in a Maze

## Problem Statement - Part 3

For example, consider the below matrix. If source = (0, 0) and destination = (7, 5), the shortest path from source to destination has length 12.

<img src = "../../Images/BFS_maze.jpg" width = "400px"> 

## Analysis

Here, the problem statement provides us with an example input. For good practice, we should make our own test cases as well to see how our high-level ideas (NOT CODE - we have not gotten there yet!) for solutions to the problem work. Running your ideas on multiple test cases helps in finding flaws in your current thinking and helps in stimulating new ways of thinking about the problem.

Here is another example of a test case that you could come up with on your own.

```
Source = (1, 1) and destination = (4, 0) Path length = 6

[0 0 1 0]
[0 1 1 0]
[0 0 1 1]
[0 1 1 0]
[1 1 1 1]
```

Notice how this test case differs from the first one. This one has a rectangular (not square) matrix and the source is not (0, 0). You should try to come up with as many distinct test cases as possible.