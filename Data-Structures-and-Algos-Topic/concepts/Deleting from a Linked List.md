<!--title={Deleting from a Linked List}-->

You’ll be happy to know that delete is very similar to search! The delete method traverses the list in the same way that search does, but in addition to keeping track of the current node, the delete method also remembers the last node it visited. When delete finally arrives at the node it wants to delete, it simply removes that node from the chain by “leap frogging” it. This means that when the delete method reaches the node it wants to delete, it looks at the last node it visited (the ‘previous’ node), and resets that previous node’s pointer so that, rather than pointing to the soon-to-be-deleted node, it will point to the next node in line. Since no nodes are pointing to the poor node that is being deleted, it is effectively removed from the list!

This method also uses a base case that checks if the list is empty or if there is only one value left in the list. It needs a separate check for these, because the while loop shown below won't work and throws an error in these cases. If the list is empty, a `ValueError` is raised, which prints the message shown below (this also prints when the method iterates through the whole list and the data value isn't in the list). When there is only one value, the method deletes that value and sets the head pointer to the value after it: None. This effectively clears the list. 

The time complexity for the delete method is O(1), because it takes the same amount of time to delete a node no matter the size of the linked list. This is because we only delete one node when we call this function, so the action is the same every time. This is the best, average, and worst case time complexity, so this method is very time efficient. 

```python
def delete(self, data):
    current = self.head
    previous = None
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            previous = current
            current = current.get_next()
    if current is None:
        raise ValueError("Data not in list")
    if previous is None:
        self.head = current.get_next()
    else:
        previous.set_next(current.get_next())
```

