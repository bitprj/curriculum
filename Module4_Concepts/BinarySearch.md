<!--title={Binary Search}-->

# What is Binary Search

Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.

### How does Binary Search Works?

For a binary search to work, it is mandatory for the target array to be sorted. We shall learn the process of binary search with a pictorial example. The following is our sorted array and let us assume that we need to search the location of value 31 using binary search.

![binary_search_0](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_search_0.jpg)

First, we shall determine half of the array by using this formula:

```
mid = low + (high - low) / 2
```

Here it is, 0 + (9 - 0 ) / 2 = 4 (integer value of 4.5). So, 4 is the mid of the array.

![binary_search_1](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_search_1.jpg)

Now we compare the value stored at location 4, with the value being searched, i.e. 31. We find that the value at location 4 is 27, which is not a match. As the value is greater than 27 and we have a sorted array, so we also know that the target value must be in the upper portion of the array.

![binary_search_2](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_search_2.jpg)

Hence, we calculate the mid again. This time it is 5.

![binary_search_5](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_search_5.jpg)

We compare the value stored at location 5 with our target value. We find that it is a match.

![Binary search](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_search_6.jpg)

We conclude that the target value 31 is stored at location 5.

Binary search halves the searchable items and thus reduces the count of comparisons to be made to very less numbers. It does this by using recursion, where the function calls itself with new parameters — this cuts the set of values we search in half. 

#### Binary Search Code

 Python Program for recursive binary search. 

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 

```python
# Check base case 
if r >= l: 

	mid = l + (r - l)/2

	# If element is present at the middle itself 
	if arr[mid] == x: 
		return mid 
	
	# If element is smaller than mid, then it 
	# can only be present in left subarray 
	elif arr[mid] > x: 
		return binarySearch(arr, l, mid-1, x) 

	# Else the element can only be present 
	# in right subarray 
	else: 
		return binarySearch(arr, mid + 1, r, x) 

else: 
	# Element is not present in the array 
	return -1
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
	print "Element is present at index % d" % result 
else: 
	print "Element is not present in array"
```

The time complexity of recursive binary search is O(1), best case. If the desired value is at the first midpoint, then the first iteration of the function is enough to find the value. The worst case time (and average case) is O(logn), since we divide the value set in half every time the function calls itself again. Space complexity is also O(logn). Binary search is the most efficient search, since the scope of the search is cut in half every time you don't find the value. 