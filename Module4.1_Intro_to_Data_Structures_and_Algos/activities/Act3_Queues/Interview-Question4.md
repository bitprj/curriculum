# Find the Shortest Path in a Maze

## Before We Start to Code

Now that we have broken down the question, seen an example test case, and come up with our own

Hints:

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
    * `row[3]` and `col[3]` taken together represent moving down.L