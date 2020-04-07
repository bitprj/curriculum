<!--title={Binary Search Tree Heaps}-->

# Binary Heaps

#### Binary Heaps:

One interesting type of tree data structure is a **Binary Heap**, which is a type of binary tree. A binary tree is a data structure where each node can have 0, 1, or 2 children, that is, nodes connected to them that are 'lower' in the tree. Binary heaps have the following properties that make them a specific type of tree:

- All nodes are completely filled, meaning they have two children, except for the last level, whose nodes can have single children so long as they are all as left-most as possible.
- New children must be added to the left-most available position.
- It is either an instance of a Min Heap or Max Heap.

A **Min Heap** is a heap where the root has the smallest key and the keys on the nodes get larger as you go down the tree. A **Max Heap** is a heap where the root has the largest key and the keys on the nodes get smaller as you go down the tree. In either case, the heap is sorted, smallest to largest or vice versa.

Examples of **Binary Heaps**:

<img src="https://www.cs.cmu.edu/~adamchik/15-121/lectures/Binary%20Heaps/pix/heap.bmp">

The image on the left is an example of a **Min Heap**. The image on the right is an example of a **Max Heap**.

Heaps are helpful when you want to find the minimum of maximum value of a data set. Since max heaps store the greatest key at the root, and min heaps store the smallest key at the root, you can use max heap or min heap when you know you always want to find the largest and lowest value, respectively.

There are two common binary heap operations: insert and delete. Let's take a look.

- **Insert** is used to add a new node into the heap. Because these heaps are ordered numerically, this operation must insert the new key into a precise location in the heap, and reorder the heap so a) the key it replaces is moved the correct location, and b) the leaf nodes on the lowest level are all still in the left-most position. In the simplest case, you only have to add a node the edge on the heap. In the most complicated case, the new node replaces the root, or top, node, changing the entire structure of the heap.
- **Delete** is similar to insert, but slightly more complicated. In must maintain the same rules — keeping leaf nodes left-most — but it recquires a specific method. Because removing from the middle of the heap is complicated, we swap the node to be deleted with the right-most leaf node, then delete the desired node (which is now a leaf node), and then move the swapped node back to it's proper position lower in the heap. Again, removing a leaf node will be easiest, but removing the root means the swapped leaf node has to move all the way back down the heap, which can take a while. 

Heaps are usually stored in an array, because the nodes can be found using arithmetic. This means that a given nodes' parent and child nodes can be found using equations, using division and mutiplication by two, which is very efficient. 

