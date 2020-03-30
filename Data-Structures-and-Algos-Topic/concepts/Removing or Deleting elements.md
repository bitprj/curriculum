<!--title={Removing or Deleting Elements}-->

There are several ways to remove or delete items from lists. 

**The `del` Keyword**

We can delete one or more items from an array using Python's `del` statement.

The syntax of the `del` statement is:

```
del obj_name
```

Here, `del` is a Python keyword, notice we don't use dot notation or parentheses to attach it to an array or argument. And, `obj_name` can be variables, user-defined objects, lists, items within lists, dictionaries, etc.

The example below will produce an output that shows the `number` array with the third element deleted.

```python
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4])

del number[2] # removing third element
print(number) # Output: signed int array with [1, 2, 3, 4]
```

> Note: the second index of an array refers to the third element.

Using the `del` function on an entire array will completely delete the array, and an interactions with the array following deletion will result in an error. Thus, `print(number)` will output an error since `number` no longer exists:

```python
del number # deleting entire array
print(number) # Error: array is not defined
```

**The `remove()` method**

We can use the `remove()` method to remove a given item in the list, that is, a specific element we want to take out.

The `remove()` method takes a single element as an argument and removes it from the list.

If the argument (in this case an element) passed to the `remove()` method doesn't exist, a ValueError exception is thrown.

**The `pop()` method**

The `pop()` method takes a single argument (index) and removes and returns the item present at that index. Note the difference between this and the remove method is that for `pop()`, we pass an index, without caring about the element at that index, to be removed. For `remove()`, we care about the element, without caring about the it's index.

`pop()` also returns the value at the given index, so it both removes an item and outputs a value. `return()` doesn't output anything.

If the index passed to the `pop()` method is not in range, it throws an IndexError: pop index out of range exception.

The parameter passed to the `pop()` method is optional. If no parameter is passed, the default index **-1** is passed as an argument, which returns the last item in the list. This is unlike `remove()`, which needs an argument.

See the use of the pop and remove methods below, and note how they differ:

```python
import array as arr
numbers = arr.array('i', [10, 11, 12, 12, 13])

numbers.remove(12)
print(numbers)   # Output: array('i', [10, 11, 12, 13])

print(numbers.pop(2))   # Output: 12
print(numbers)   # Output: array('i', [10, 11, 13])
```

Notice that for `number.remove(12)`, there were two elements of 12 in the array. When this is the case, the first corresponding element it finds is removed, so you can think about it as the first of the two 12's being deleted. 

