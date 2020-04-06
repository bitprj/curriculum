# Find the Shortest Path in a Maze

Rather than presenting the problem statement all together, we will present this problem in significant chunks, so that we can break down and analyze each part of the question.

## Problem Statement - Part 1

Given a maze of the form of a rectangular matrix, develop an algorithm to find the length of the shortest path from a given source to a given destination.

## Analysis

Here, we are given the general goal of our problem, without any of the specific implementation details that will be presented later. We should use this information to ensure that we have a foundational understanding of what we are required to do.

Let's break down the information line-by-line.

* "Given a maze of the form of a **rectangular matrix**"
  * This is an indicates that the medium of our maze will be a 2D list. Immediately, you should ask yourself
    * How does this impact the way we move through the maze? Can we move diagonally? Can we wrap around the top? Is there any restriction on where we start from and where we end?
* "develop an algorithm to find the length of the **shortest path** from a given **source to a given destination**."
  * A light bulb should go off when you see the phrase "shortest path" You should ask yourself:
    * What well-known algorithms have I seen in the past that use "shortest path" in their problem statement (hint: famous graph algorithms). What data structures do those algorithms use and will they be any use to me here (they may or may not)?  