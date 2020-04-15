<!--title={The Linked List}-->

### The Linked List

The linked list is a data structure involving nodes and pointers. It is a linear data set than holds nodes in sequence, with each pointing to the next node. This doesn't make them ordered; unlike arrays, linked lists don't have indices, so search isn't as simple as it is in arrays. They are useful for efficient deletion and insertion of elements in the list, by the simple movement of pointers to new or different nodes.

A simple implementation of a linked list includes the following methods:

- Insert: inserts a new node into the list

  The insert() function takes two parameters:

  - **index** - position where an element needs to be inserted
  - **element** - this is the element to be inserted in the list

- Size: returns size of list

- Search: searches list for a node containing the requested data and returns that node if found, otherwise raises an error

- Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error


**The Head of the List**

The first architectural piece of the linked list is the ‘head node’, which is simply the first node in the list. When the list is first initialized it has no nodes, so the head is set to None. (Note: the linked list doesn’t necessarily require a node to initialize. The head argument will default to None if a node is not provided, as shown by `head=None` in the constructor method's arguments.)

```python
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
```

**The Tail of the List**

Another useful piece is the tail of the list. This is the last node in the list. It's not necessary to have this node tracked, but it makes some operations easier later (like deleting the last node). The linked list will never require a tail to initalize, and at first, the head and the tail will point to the same, single value in the list. Once more values are added, the tail will only point to the last value. Again, a tail argument will never be passed, so this is just here to track the last value. 

```python
class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
```

