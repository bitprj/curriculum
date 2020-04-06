# Find the Shortest Path in a Maze

## Problem Statement - Part 2

The path can only be constructed out of cells having a value of `1` and, at any given moment, we can only move one step in one of the four directions. The valid moves are:

* Go Up: (x, y) --> (x - 1, y)
* Go Left: (x, y) --> (x, y - 1)
* Go Down: (x, y) --> (x + 1, y)
* Go Right: (x, y) --> (x, y + 1)

## Analysis

We are provided with a **lot** of useful information here. Most importantly, we now know how our matrix will be formatted and in what directions we can move.

At this point, you should ponder about what each of the coordinates for each of the respective moves represents. More specifically,

* Why do "Go Up" subtract 1 from the x-coordinate and "Go Down" add one to the x-coordinate. Why does neither impact the y-coordinate instead?
* Why do "Go Left" subtract 1 from the y-coordinate and "Go Right" add one to the y-coordinate. Why does neither impact the x-coordinate instead?

The above points should make you consider alternatives for storing the (x, y) coordinates. Should you store them as tuples? Should you have different arrays for the x coordinates and y coordinates? Does it matter?

This is a good example of when drawing a diagram of the problem setup (2D list) is helpful in visualizing the problem and seeing why certain properties hold. Although the next section will provide you with a diagram, you should get into the habit of making diagrams, especially considering that problem statements usually only provide the most basic diagrams and test cases. 