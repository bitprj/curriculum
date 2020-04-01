<!--title={Deleting dictionary elements}-->

To delete from dictionaries, you can either remove individual dictionary elements or clear the entire contents of a dictionary. You can also delete an entire dictionary in a single operation. 

We can remove a particular item in a dictionary by using the method `pop()`. This method takes a key as an argument, removes the (key, value) pair, and returns the value at that key. 

The method `popitem()` can be used to remove and return the last (key, value) pair from the dictionary. It takes no arguments, and returns both the key and value.

 All the items can be removed at once using the `clear()` method.

We can also use the `del` keyword to remove individual items or the entire dictionary itself.

```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'School': 'DPS School'}
del dict['Name']; # remove entry with key 'Name'

print(dict)
```

The code snippet above should output the entire dictionary `dict` without the `Name` key and its value.

```python
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary
```

> Note: _clear()_ function will delete all (key, value) pairs within the dictionary _dict_, but _dict_ will still exist as an empty dictionary. 
>
> Note: using the _del_ function on the entire dictionary means _dict_ will no longer exist as it would be completely deleted. 



The average case time complexity of deleting an item from a dictionary is O(1). This is because every time you delete an element, you only ever give one argument, and the same operation is done every time, making it take a constant time. 