<!--title={Quick Sort}-->

# Quick Sort 

Quick Sort is one of our four sorting algorithms, and it is known as the most efficient and fastest of the four. Similar to Merge Sort, Quick Sort also uses recursion in its implementation.

### Implementation of Quick Sort:

1. Determine a **pivot** point, which would be an element in the dataset, and according to GeeksforGeeks, there are many ways to choose a pivot. For instance, always choosing the first element, last element, middle element, or even choosing a random element.
2. Using the pivot point, *partition* (or divide) the larger unsorted collection into two, smaller lists. 
3. Sort the unsorted collection into two groups. Everything smaller is moved to the right/or left of the pivot point, and everything greater would be moved to the opposite direction of the pivot point.
4. Then choose another pivot point with in that subgroup. 
5. Repeat this process until the entire data structure is organized. 
6. Recombine all the subgroups back into one big group so the data structure is now organized. 

![img](http://cdn.differencebetween.net/wp-content/uploads/2018/11/Difference-between-Quick-Sort-and-Merge-Sort.png)

Now that we understand how Insertion Sort works, let's look at some pseudocode, modified from the Programiz website, that demonstrates an implementation of this sorting algorithm:

```
quicksort(array, left most index, right most index)
  if (left most index < right most index)
    pivot index <- partition(array, left most index, right most index)
    quicksort(array, left most index, pivot index)
    quicksort(array, pivot index + 1, right most index)

partition(array, left most index, right most index)
  set right most index as pivot index
  storeIndex <- left most index - 1
  for i <- left most index + 1 to right most index
    if element[i] < pivot element
      swap element[i] and element[storeIndex]
      increment store index
  swap pivot element and element[store index + 1]
return store index + 1
```

### Important Characteristics of Quick Sort:

* The best and average case time complexity of Quick Sort is Θ(nlogn), which happens when the partitions are closely or equally sized.
* The worst case time complexity of Quick Sort is Θ(n^2), which happens when we have the most unbalanced partitions possible.
* The space complexity of Quick Sort is O(logn) because space is needed when the partition with the fewest elements is sorted first through recursion.

