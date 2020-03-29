# concept_name
Separate Chaining

# Separate Chaining Step 1

## name
```
Separate Chaining With Hash Tables
```

## md_content
```
# Separate Chaining when working on Hash tables

When working with **Hash functions**, it is inevitable that the hash function will assign the same HashTable index to multiple inputs since our Hash table only has a finate number of spaces in it. 
As we can have an infinite number of inputs, the Hash function can assign the same index in our Hash table to multiple inputs
This is a problem because a Key-Value pair should be unique in order to have an efficient Hash table. 
```

# Separate Chaining Step 2

## name
```
How Separate Chaining is Implemented
```

## md_content
```
To alleviate this problem, what we can do is implement linked lists in our Hash table. In each index in our Hash table, we can store a linked list that points to every input that is stored in that index.
This means that when we access our index values in a Hash table, we also need to search through the linked list associated with the index value. 
```
## image
![alt](https://projectbit.s3-us-west-1.amazonaws.com/darlene/labs/Screen+Shot+2020-03-24+at+3.15.53+PM.png)

# Separate Chaining Step 3

## name
```
Separate Chaining Example
```

## md_content
```
Say that multiple inputs are assigned to the same index 3. Before we implemented a linked-list, if we were to try and reference that index in our hashtable, we'd run into a problem as multiple inputs are stored there.
However, with Chaining, we are able to link all the inputs stored in that index with a linked list. If we wanted to access a specific value in the linked-list, what we would need to do is navigate through the linked list until we find the value we want. 
By implementing linked lists into our Hash Tables, we are able to allocate memory dynamically which fixes our issue of Collision. 
```
