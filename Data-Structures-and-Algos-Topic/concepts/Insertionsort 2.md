<!--title={Insertion Sort}-->

# Insertion Sort

Insertion Sort is another one of our four basic sorting algorithms, and it is unique in a sense that is similar to how one would sort playing cards in a hand. 

### Implementation of Insertion Sort:

1. Compare the first element with the second element. If the element is smaller, move the first element past the second element. 
2. Keep comparing the "first" element with the next elements, passing smaller elements, until we reach an element that is greater than it. 
3. *Insert* that element in that place holder, and start again for the beginning.
4. Repeat this process until the entire array is sorted.

![alt](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

Now that we understand how Insertion Sort works, let's look at some pseudocode, modified from the Programiz website, that demonstrates an implementation of this sorting algorithm:

```
insertionsort(array)
  mark first element as sorted
  for each unsorted element X
    extract the element X
    for j = last sorted element's index down to 0
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
```

### Important Characteristics of Insertion Sort:

* Insertion sort is most useful when working with data sets that are small or are partially sorted through with only a few misplaced items.
* The best time complexity of Insertion Sort is O(n), which occurs when the array is already sorted.
* The worst time complexity of Insertion Sort is O(n^2), which occurs when the array is in reverse order.
* The space complexity of Insertion Sort is O(1) because one element is moved and compared per iteration.



