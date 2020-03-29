<!--title={Updating dictionary}-->

Dictionaries are mutable. We can add new items or change the value of existing items using assignment operator.

You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown below in the simple example −

```python
# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
```

> Note: a dictionary allows you to dynamically add new keys with corresponding values or redefine values to an existing key following initialization.

The code snippet above should reflect the appropriate changes on _dict_ such that it contains a new key _'School'_ and that _'Age'_ no longer has value _'7'_.

To delete an item from an dictionary, we use the keyword **del**. See below:

```python
del dict['Name']
```

You pass the key in the brackets, and this deletes the key value pair. 

When there are multiple values associated with a key, the deletion is slightly more involved. Here is an example of a dictionary with mutiple values:

```python
dict = {'Name': ('Zara', 'Golde'), 'Age': 7, 'Class': 'First'}
```

As you can see, there are two names listed after the key 'Name'. To delete only one of these values, we use two brackets. The first one denotes the key, and the second denotes the index of the value you'd like to delete.

```python
del dict['Name'][1]
```

The above deletion would remove 'Golde' from the values, since 'Zara' is at index 0, and 'Golde' is at index 1. 

The best case time complexity for updating dictionaries is O(1), since these operations happen in constant time. Worst case is O(n), when the underlying storage has to be changed to accomodate the new key value pair. Space complexity is O(n), when n is the number elements, since the size of the dictionary depends on the number of elements therein. 

