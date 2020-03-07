<!--title={Merge Sort}-->

# Merge Sort

Merge Sort is a sorting algorithm that uses recursion, which means it calls upon itself, and we use sorting algorithms like Merge Sort to make our data more manageable. 

When given an array of elements, Merge Sort starts by dividing the array into two separate sections. Then, it will divide those two sections in half and will continue to do so until it reaches its base case (each element is standing on its own). Once this is done, Merge Sort begins to *merge* the adjacent elements together into pairs, sorts them, and repeats this merging process with the resulting pairs and so on until a sorted list remains. A visual demonstration is shown below:

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

### Important Characteristics of Merge Sort:

- Merge Sort is useful for sorting linked lists.
- The time complexity of Merge Sort is Θ(nlogn) for worst, average, and best case because dividing the array takes logn times and each pass through the array is proportional to its number of elements, n.
- The space complexity of Merge Sort is O(n), which shows that this algorithm takes a lot of space and may slow down operations for its last data sets.

