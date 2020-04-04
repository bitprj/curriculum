<!--title={Queue Manipulation}-->

# Adding and Removing Items from a Queue

### Goals

In this concept, we will learn about the most important functions of a Queue data structure: adding an item to the queue, subtracting an item from the queue, and viewing the queue.

### Adding an Item 

To add an item to a queue, we need to create a function `def enqueue()`. 

```python
def enqueue(self, item):
	self.item.append()
```

We can call this function by simply using the line of code 

```python
Queuename1.enqueue(Item1)
```

This adds an item to the **end** of the queue. This is analogous to adding someone to the end of a line at a concert.

### Removing an Item

To remove an item from a queue, we also need to write a function. 

```python
def dequeue(self, item):
    return self.items.dequeue()
```

This removes an item from the **front** of the queue. This is analogous to someone being at the front of the line for a concert and being admitted in and removed from the line in order to go enjoy the show!

### To view a queue

The function we write to do this will be a for loop that prints out every element in our queue.

```python
for i in range (len(self.queue)):
	print (self.queue[i])
```

This loops through all of the elements that are **currently in** our queue and prints them out. This is analogous to a security guard checking each person that is in the concert line. The guard won't be checking the people who have already been admitted into the concert (i.e. people who have been dequed) nor checking those who haven't entered the line (haven't been enqueued); the guard will only check those **currently in** line.



