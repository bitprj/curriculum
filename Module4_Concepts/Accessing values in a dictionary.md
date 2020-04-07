<!--title={Accessing values in a dictionary}-->

To access dictionary elements, you can use the familiar square brackets [] along with the key to obtain its value.

Looking up or setting a value in a dict uses square brackets, e.g. dict['foo'] looks up the value under the key 'foo'. Strings, numbers, and tuples work as keys, and any type can be a value. Other types may or may not work correctly as keys (strings and tuples work cleanly since they are immutable). Looking up a value which is not in the dict throws a KeyError -- use "in" to check if the key is in the dict, or use dict.get(key) which returns the value or None if the key is not present (or get(key, not-found) allows you to specify what value to return in the not-found case).

```python
# Declare a dictionary 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
```

> Note: remember the dictionary is structured as (key, value) pairs such that the **keys** in _dict_ are _'Name', 'Age', 'Class'_ and **values** are _'Zara', '7', 'First'_ respectively.

The code snippet above should produce a result such that the values to the keys, *'Name'* and *'Age'*, within the _dict_ are printed.

Dictionaries can have multiple values associated to a single key. This can either be represented as a set of values per key or a list of values per key. However, a key must have values of the **same** data type. 

A for loop on a dictionary iterates over its keys by default. The keys will appear in an arbitrary order. The methods dict.keys() and dict.values() return lists of the keys or values explicitly. There's also an items() which returns a list of (key, value) tuples, which is the most efficient way to examine all the key value data in the dictionary. All of these lists can be passed to the sorted() function.

Now for values as a set per key which puts the values of each key in curly braces *{ }*, they are represented as a distinct list of unordered elements:

```python
dict1 = {'ints':{2,1,3}, 123:{'apple', 'banana', 'carrot'}}
for x in dict1['ints']:
    print(x)
for x in dict1[123]:
  	print(x)
```

> Note: **Sets** automatically sort their **integers** in ascending order, but leave their **strings** in a random order from when they were initialized.

All the values for each key are of the same data type, all values for *'ints'* are of integer data type and all values for *123* are of string data type. 

To access an element, the Big O time complexity is on average O(1), since it takes the same amount of time to find it no matter the size of the dictionary. Worst case time complexity is O(n), where the time it takes to access an element depends on the size of the dictionary.