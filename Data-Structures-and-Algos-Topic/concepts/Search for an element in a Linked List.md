<!--title={Search for an element in a Linked List}-->

Search is actually very similar to size, but instead of traversing the whole list of nodes it checks at each stop to see whether the current node has the requested data and if so, returns the node holding that data. If the method goes through the entire list but still hasn’t found the data, it raises a value error and notifies the user that the data is not in the list.

The time complexity of search is O(n) in the worst case.

```python
def search(self, data):
    current = self.head
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            current = current.get_next()
    if current is None:
        raise ValueError("Data not in list")
    return current
```

---

###Search an element in a Linked List (Iterative and Recursive)

Write a function that searches a given key ‘x’ in a given singly linked list. The function should return true if x is present in linked list and false otherwise.

```python
   bool search(Node *head, int x) 
```

For example, if the key to be searched is 15 and linked list is 14->21->11->30->10, then function should return false. If key to be searched is 14, then the function should return true.

**Iterative Solution**

```
1) Initialize a node pointer, current = head.
2) Do following while current is not NULL
    a) current->key is equal to the key being searched return true.
    b) current = current->next
3) Return false 
```

**Recursive Solution**

Keep in mind that this method is not as commonly used as the Iterative Solution.

```
1) If head is NULL, return false.
2) If head's key is same as x, return true;
2) Else return search(head->next, x) 
```

