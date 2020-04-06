# Find the Shortest Path in a Maze

## Before We Start to Code

Now that we have broken down the question, seen an example test case, and come up with our own, we are ready to come up with a code-specific algorithm.

You should realize that

* For whatever move we make, we are going to have to check if its valid. We don't want to be allowed to go up when we are in the first row, we don't want to go left if in the first column, etc. This means we should have a `isValid()` function.
* We have to store which portions of the maze we have already visited. We also have to be able to fully "explore" a possible path. This should remind you of a certain, well-known graph algorithm.

Here are some specific hints about how to approach this problem:

* BFS will be a useful algorithm to familiarize yourself with

* Initialize the following two arrays in your code

  * ```python
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]
    ```

  * Creating `row` and `col` as such allows us to represent the four possible moves (up, left, down, and right) that one can make.

    * `row[0]` and `col[0]` taken together represent moving up.
    * `row[1]` and `col[1]` taken together represent moving left.
    * `row[2]` and `col[2]` taken together represent moving right.
    * `row[3]` and `col[3]` taken together represent moving down.