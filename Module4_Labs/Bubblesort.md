<!--title={Bubblesort}-->

# Bubblesort

Bubblesort is the simplest of the four types of sorting algorithms we will be going over in this lab since it only uses swapping to sort through the entire list.

### Implementation of Bubblesort:

1. Compare the first two numbers, and if they are not sorted, then swap the two.
2. Move on to the second and third values, compare the two numbers, then swap if necessary.
3. Repeat this process to the end of this list, until the last pair of numbers are sorted.
4. Start again from the first number and continue this process until the entire list is sorted.

![Image result for bubble sort image](https://algonomics.io/images/bubble-sort/BubbleSort.PNG)

Now that we understand how Bubblesort works, let's look at some pseudocode, modified from the Programiz website, that demonstrates an implementation of this sorting algorithm:

```
mergesort(array):
	for i = 1 to index of last sorted element:
		if left element > right element:
			swap left element and right element
```

### Important Characteristics of Bubblesort:

* Bubblesort is useful for rearranging values very quickly.
* The best time complexity for Bubblesort is O(n), which happens when the array is already sorted.
* The average and worse time complexity of O(n^2), which happens when the numbers in the array are in reverse order (decreasing, rather than increasing).
* The space complexity for Bubblesort is O(1) because there only needs to be additional memory space for the temporary variable used for swapping two elements.





