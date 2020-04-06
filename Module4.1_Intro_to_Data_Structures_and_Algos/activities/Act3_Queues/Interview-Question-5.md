# Find the Shortest Path in a Maze

## Code Analysis

After coding the problem yourself (or seeing the solution provided), it is important to do an analysis of your solution for time and space complexity.

### Time Complexity

The `isValid()` function is `O(1)`, so the time complexity is driven by our `BFS()` function. What is the worst case that this function can undergo? Well, we would require the most processing every single element of our 2D list.

Now that we have identified our worst case scenario, how would the processing of this scenerio change with the input size (as our input gets larger and larger)? Well, if we are enqueuing and processing every element of our matrix and the number of elements is always (`# of rows * # of columns`), that means our worst case processing should always be (`# of rows * # of columns`). That is, our worst case time complexity is `O(RC)`, where `R = # of rows` and `C = # of columns`.

### Space Complexity

For space complexity, we have to identify our data structure that requires the most space/memory. In this case, the matrix we create requires the most space and is of size `R*C`. Thus, our worst case space complexity is `O(RC)` as well!

