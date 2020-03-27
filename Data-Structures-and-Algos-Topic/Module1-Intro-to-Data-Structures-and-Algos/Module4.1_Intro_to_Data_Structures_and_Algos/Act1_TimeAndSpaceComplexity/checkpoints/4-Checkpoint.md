# name
 Time Complexity

 # cards_folder
 Module4.1_Intro_to_Data_Structures_and_Algos/activities/Act1_TimeandSpaceComplexity

 # checkpoint_type
 multiple choice

 # instruction
 Select the correct time complexity for the given codes 

 ```python
 print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
 ```

 # mc_choices
 ## choice_1
 linear
 ## choice_2
 constant
 ## choice_3
 quadratic
 # correct choice
 linear 



 ```python
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
 ```

 # mc_choices
 ## choice_1
 linear
 ## choice_2
 constant
 ## choice_3
 quadratic
 # correct choice
 Quadratic



 ```python
 num = int(input("Enter a number: "))  
 if (num % 2) == 0:  
    print("{0} is Even number".format(num))  
 else:  
    print("{0} is Odd number".format(num))  
 ```

 # mc_choices

 ## choice_1

 linear

 ## choice_2

 constant

 ## choice_3

 quadratic

 # correct choice

 constant 
