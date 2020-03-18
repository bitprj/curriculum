<!--title={The Node}-->

The node is where data is stored in linked lists, trees, and graphs. (they're kind of like those plastic Easter eggs that hold treats). Along with the data, each node also holds a pointer which is a reference to the next node in the data structure. Below is a simple implementation of a `Node` class:

```python
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node 

    def set_next(self, new_next):
        self.next_node = new_next
```

> This class _Node_ represents the node objects that are within a given data structure. Each _Node_ contains data that can be retrieved via the `get_data` function and can set or get the next node via the functions `set_next` and `get_next` respectively.

The node initializes with a single datum and its pointer is set to None by default (this is because the first node inserted into the list will have nothing to point at!). We also add a few convenience methods: one that returns the stored data, another that returns the next node (the node to which the current object node points), and finally a method to reset the pointer to a new node. These will come in handy when we implement Linked Lists and Search Trees.