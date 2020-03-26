# Find the Shortest Path in a Maze

Given a maze of the form of a rectangular matrix, develop an algorithm to find the length of the shortest path from a given source to a given destination.

The path can only be constructed out of cells having a value of `1` and, at any given moment, we can only move one step in one of the four directions. The valid moves are:

* Go Up: (x, y) --> (x - 1, y)
* Go Left: (x, y) --> (x, y - 1)
* Go Down: (x, y) --> (x + 1, y)
* Go Right: (x, y) --> (x, y + 1)

For example, consider the below matrix. If source = (0, 0) and destination = (7, 5), the shortest path from source to destination has length 12.

<img src = "../../Images/BFS_Maze.jpg" width = "400px"> 

Hints:

* BFS will be a useful algorithm to familiarize yourself with

* Initialize the following two arrays in your code

  * ```python
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]
    ```

  * Creating `row` and `col` as such allows for us to represent the four possible moves (up, left, down, and right) that one can make.

    * `row[0]` and `col[0]` taken together represent moving up.
    * `row[1]` and `col[1]` taken together represent moving left.
    * `row[2]` and `col[2]` taken together represent moving right.
    * `row[3]` and `col[3]` taken together represent moving down.