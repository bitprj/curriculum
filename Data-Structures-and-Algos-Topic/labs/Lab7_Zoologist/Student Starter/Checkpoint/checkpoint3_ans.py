def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

def selectionSort(arr):
    # Traverse through all array elements 
    for i in range(len(arr)): 
      
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)

def main():
    arr = [9, 12, 4, 19, 10, 3]
    print('Original List: ', arr)
    print('List sorted by Bubble Sort: ', bubbleSort(arr))
    print('List sorted by Insertion Sort: ', insertionSort(arr))
    print('List sorted by Selection Sort: ', selectionSort(arr))

main()