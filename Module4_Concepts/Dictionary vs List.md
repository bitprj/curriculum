<!--title={Dictionary vs. List}-->

Though they are both different data structures; both are dynamic in nature and can grow as required. Now that we have covered both dictionaries and lists, you're probably wondering: "when do I use one or the other?"

**List** is like an array of sequential values with some order such as:

```python
List = [1, 2, 3, 4, 5]
```

Lists are useful for storing and retrieving elements by that order or by the index. You can also loop through the list by sequence of indices.



**Dictionary** is basically a hash table where its elements are a <key, value> pair. Keys and values can be an integer, string or character. 

```python
Dict = {'a': 2, 'c': 5}
```

It's particularly useful to retrieve the values based on their keys, when there in no particular order in the values such as:

```python
Dict['a'] # which is equivalent to accessing the value 2
```

This kind of indexing is not possible in lists. It's useful for quick retrieval or checking whether a key exists or not, or what's the corresponding value. The same operation in a list would involve a linear search of the complete list in worst case thus making a list inefficient for this kind of operations.

---

This is a table comparing the time and space complexities of lists and dictionaries for different functions:

![complexities chart](complexities chart.jpg)