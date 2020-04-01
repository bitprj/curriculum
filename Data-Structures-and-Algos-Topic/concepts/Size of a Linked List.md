<!--title={Size of a Linked List}-->

The size method is very simple. It counts the nodes until it can’t find any more, and returns how many nodes it found. The method starts at the head node and travels down the line of nodes, adding 1 to the count each time. When the tail is reached, it adds 1, and then the tracking variable `current` is set to None, since the value after the tail is None. At this point the while loop is exited and the final count is returned. 

```python
def size(self):
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.get_next()
    return count
```

The time complexity of size is O(n) because each time the method is called it will always visit every node in the list but only interact with them once, meaning n * 1 operations, n being the number of nodes. 

