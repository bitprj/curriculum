
## Multiple Choice Checkpoint

Description: What would `printList()`  look like ?

Choices:
```python
def printList(self, node): 
    while node != None: 
        print(node.data)
        node = node.next
```


```python
def printList(self, node): 
    for i in range(len(node)):
        print(node[i].data)
```

```python
def printList(self, node):
    print(node)
    printList(node.next)
```



 
Correct Choice:

```python
def printList(self, node): 
    while node != None: 
        print(node.data)
        node = node.next
```