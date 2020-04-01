<!--title={Binary Search Trees}-->

# Binary Search Trees

A **Binary Search Tree (BST)** is a data structure that holds data in nodes. The nodes are formed in a hierarchy that forms the 'tree' as shown below. Parent nodes can have children, which can also be parents to their own children, forming the tree structure. BSTs also have a few more requirements.

##### BST Rules:

* Each node in the tree can have only 0, 1, or 2 children.
* Every node in the left subtree of a parent node has keys that are lower in number than the key of that parent node. This includes all nodes, not just the immediate left child node.
* Every node in the right subtree of a parent node has keys that are higher in number than the key of that particular node. This includes all nodes, not just the immediate right child node.

Let's see an example of a valid vs invalid BST:

<img src="https://i1.wp.com/algorithms.tutorialhorizon.com/files/2014/09/Invalid-BST.png?ssl=1" width="250">

<img src="https://i0.wp.com/fitcoding.com/wp-content/uploads/2016/10/720px-Binary_search_tree.svg_.png" width="250">

Are you able to tell which tree is a valid BST and which is invalid?

The **top** tree is an **invalid** BST because the node containing the key 10 is in a right subtree of the node containing the key 30. Likewise, the bottom tree is valid since it abides by all the BST rules. You may have noticed that all subtrees of a BST are also BSTs. 

In order to implement a BST in Python, we just need to adjust our previous `Node` class.

```Python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
```

Since we know that BST nodes only have two children max, we no longer need a list to store the children; we simply store the left child as the **left** element and the right child as the **right** element. In the `Node` class the left and right children are initialized to null.

BSTs can be implemented as arrays or as linked lists. When implemented as arrays, children nodes of a parent node with index 'k' are easily found with the algorithm 2k and 2k+1, to find left and right children respectively. Arrays can only represent complete trees, or trees whose nodes each have two children, except for the last level where all leaf nodes must be as left-most as possible. This representation is useful for searching for nodes.

When implemented as linked lists, the BST doesn't need to be complete, but you can't find nodes at given indices since linked lists aren't ordered with indices like the array data structure is. Linked list BSTs are useful for adding or removing certain nodes, because the use of pointers allows for easy altering of the node sequence. 

BSTs are useful because you can use the binary search to locate elements in the tree. They are also useful when they are implemented as a binary heap, where the elements are ordered by key value, either smallest to largest or vice versa, making the search for the minimum or maximum value very efficient. BSTs can also be used to implement other data structures. These concepts will be discussed later, but it's good to keep in mind why we want to use these tools. 