<!--title={Accessing arrays}-->

We use indices to access elements of an array:

```python
a = arr.array('i', [1, 3, 8, 23, 99])
print("First element:", a[0])
print("Second element:", a[1])
print("Third element:", a[2])
print("Last element:", a[4])
print("Last element:", a[-1])
```

> Note: negative indexing means that you count from right to left which implies you start from the end of the list. In this case, _a[-1]_ and _a[4]_ are equivalent since they both access the last element of the list.
>
> Note: remember, the index starts from 0 (not 1), similar to lists.

In the example above, you can access a particular array element by specifying an *index* within the array. The array *a* contains the elements *1, 3, 8, 23, and 99* with the corresponding indices *0, 1, 2, 3, and 4*.

What happens when you try to access an index that isn't in the array?

```python
print("Fifth element:", a[5])
```

In the array we've created, there are only 5 elements, so there's no 5th index (only indices 0-4). Thus, we get an error message:

```python
IndexError: list index out of range
```

An index error is thrown because the index we are trying to access an index that doesn't exist in the array.

The Big O time complexity is O(1). This is because the search takes the same amount of time no matter how much data is in the set. In other words, it's constant. 