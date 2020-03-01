<!--title={Binary Search Tree Insert}-->

# Binary Search Tree Insert

When working with Binary Search Trees (BST), a useful tool to have is to be able to insert/add nodes to the tree.

#### BST Insert:

When adding a new node to a BST, we must make sure to find the correct place to insert that node. Let's look at the code for `BSTInsert`:

```Python
def BSTInsert(curNode, newNode):
    if curNode is None:
        curNode = newNode
    else:
        if curNode.key < newNode.val:
            if curNode.right is None:
                curNode.right = newNode
            else:
                BSTInsert(curNode.right, newNode)
        else:
            if curNode.left is None:
                curNode.left = newNode
            else:
                BSTInsert(curNode.left, newNode)
```

`BSTInsert` traverses through the BST in a similar way to `BSTSearch`. However, once it finds that the specific child is null in the place the new node belongs, it places that node there. It does this by checking if the value of the new node is greater or less than the node it's currently being compated to. If the new node value is greater, it will try to insert it to the right. Otherwise, it's smaller, and it will be inserted to the left of the next largest node value. 

The time and space complexity is O(h), where h is the height of the tree. The more nodes in the tree, the more values to be compared to, thus taking up more time and space. The worst case time is O(n).

Try working and experimenting with the code on your own machine.