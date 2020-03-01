<!--title={Adding or Changing Elements}-->

Arrays are mutable; their elements can be changed or added to in a way similar to lists.

We can add one item to a list using the `append()` method, or add several items using `extend()` method.

```append()```: Adds its argument as a single element to the end of a list. The length of the list increases by one.

```extend()```: Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in its argument.

```python
numbers = arr.array('i', [1, 2, 3])

numbers.append(4)
print(numbers)     # Output: signed int array with list [1, 2, 3, 4]

# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7]) 
print(numbers)     # Output: signed int array with list [1, 2, 3, 4, 5, 6, 7]
```

> Note: both the *append*() and *extend()* functions will concatenate the specified number(s) to the end of the existing array.

The time and space complexities of `append()` are both O(1).

We can concatenate two arrays using the `+` operator.
`+` Addition : Adds the values on either side of the operator.

```python
import array as arr
odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])
numbers = arr.array('i')   # creating empty array of integer
```

Now that we have two int arrays `odd`and `even`, we can now combine them into a single array which will be represented by the array *numbers*.

```python
numbers = odd + even
print(numbers) # Output: signed int array with [1, 3, 5, 2, 4, 6]
```

Notice that the *numbers* array starts with the elements of the *odd* array and is followed by the elements of the *even* array.

To change elements in an array, we index it to where we would like to insert an element. Then, we assign the value at that index to a new value that will replace it. 

```python
numbers[2] = 7
```

Now, the value in the array `numbers` that was at the 2nd index (5) will be a 7. 

The time and space complexity of this operation is O(1).