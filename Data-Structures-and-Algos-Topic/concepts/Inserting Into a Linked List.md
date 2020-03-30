<!--title={Inserting Into a Linked List}-->

This insert method takes data, initializes a new node with the given data, and adds it to the linked list. Technically you can insert a node anywhere in the list, but the simplest way to do it is to place it at the front of the list and point the new node at the old head, making the new node the new head (sort of pushing the other nodes down the line).

As for time complexity, this implementation of insert is constant O(1) (efficient!). This is because the insert method, no matter what, will always take the same amount of time: it can only take one data point, it can only ever create one node, and the new node doesn’t need to interact with all the other nodes in the list. The inserted node will only ever interact with the head.

```python
def insert(self, data):
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
```



**Inserting a node at a specific position in a linked list**

Given a singly linked list, a position, and an element, the task is to write a program to insert that element in a linked list at a given position. Note that position is different from index, that is, there is no 0th position as there is with indices. So position 2 is the second item in the list, no the third.

**Examples:**

```
Input: 3->5->8->10, data = 2, position = 2
Output: 3->2->5->8->10

Input: 3->5->8->10, data = 11, position = 5
Output: 3->5->8->10->11
```

**Approach:** To insert a given data at a specified position, the algorithm below should be followed:

- Traverse the linked list up to *position-1* nodes (this is the position right before the desired position).
- Once you've reached the *position-1* node, allocate the memory and the given data to the new node.
- Point the next pointer of the new node to the next of current node.
- Point the next pointer of current node to the new node.
- Base cases:
  - When the list is empty, simply add the new node to the head of the list. 
  - When the specified position isn't in the list, throw an error and ask for a new position. 