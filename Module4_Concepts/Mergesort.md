<!--title={Mergesort}-->

# Merge Sort

Merges Sort is a sorting algorithm that uses recursion, which means it calls upon itself, and we use sorting algorithms like Merge Sort to make our data more manageable. 

### Implementation of Merge Sort:

1. Given an array of elements, start by dividing the array in half into two separate sections. 
2. Divide those two sections in half and will continue to do so until it reaches its base case (each element is standing on its own). 
3. *Merge* the adjacent elements together into pairs and sort them in increasing order.
4. Repeats this merging process with the resulting pairs and so on until a sorted list remains. 

![]( https://miro.medium.com/max/3207/1*aJ1YiME33o0dBZTCmid7iw.png )

Now that we understand how Merge Sort works, let's look at some pseudocode, modified from the GeeksforGeeks website, that demonstrates an implementation of this sorting algorithm:

```
mergesort(array):
	if length of array > l: # base case

		# dividing array into elements
		find the middle point (m)
		divide the array into two halves  
    
		# sort elements in array
		call mergesort for first half    # sort first half
		call mergesort for second half   # sort second half

		# merging elements in array
		merge the two halves sorted
```

As we can see from the visual representation and pseudocode, Merge Sort merges elements in specific way. With the resulting list of the inputted array's individually separated elements, Merge Sort starts by merging two elements from both ends, front and back, into sorted pairs. At this point, there should be two sorted pairs in this list—one pair of the first two elements and another of the last two elements. It will continue by adding on the next element, from the front and back, to the pairs, making a sorted set of three. Then, Merge Sort will continue the process until the two resulting halves merge together to finally form a sorted array.

### Important Characteristics of Merge Sort:

- Merge Sort is useful for sorting linked lists.
- The time complexity of Merge Sort is Θ(nlogn) for worst, average, and best case because dividing the array takes logn times and each pass through the array is proportional to its number of elements, n.
- The space complexity of Merge Sort is O(n), which shows that this algorithm takes a lot of space and may slow down operations for its last data sets.

