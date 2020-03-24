<!--title={Matchsticks to Square: Base Cases}-->

Let's start by determining the base cases for this problem and forming with a method to approaching this problem:

Considering that we are trying to form a square, this problem boils down to splitting the given input array of integers into four subsets where all of these subsets are:

- *mutually exclusive*, or have no specific element of the array is shared by any two of these subsets
- have the same value as the total sum, which represents the length of the equal sides of the square

**Base Cases:**

- When there are no matchsticks at all
- When the total sum of all given matchsticks is not divisible by 4, implying that having four subsets of equal value are not possible 

---

First, we will determine the parameter and variables of our function `makesquare()`. Remember that the input we are given is an array of integers that represent the lengths of each matchstick, so in order to know how many matchsticks we have in total, we need to find the length of the array. 

```python
def makesquare(nums):
	L = len(nums)					  # Number of matchsticks we have
	perimeter = sum(nums)			   # Perimeter of the square (if one can be formed)
	possible_side =  perimeter // 4		# Possible length of the sides of the square
```
Then, we will set our base cases, which we determined above. 

```python
    # If there are no matchsticks, a square cannot be formed
    if not nums:
        return False

    # If the perimeter cannot be equally split by 4, a square cannot be formed
    if possible_side * 4 != perimeter:
        return False
```
---

Now, this is what we should have so far!

```python
def makesquare(nums):
	L = len(nums)					  # Number of matchsticks we have
	perimeter = sum(nums)			   # Perimeter of the square (if one can be formed)
	possible_side =  perimeter // 4		# Possible length of the sides of the square
    
    # If there are no matchsticks, a square cannot be formed
    if not nums:
        return False

    # If the perimeter cannot be equally split by 4, a square cannot be formed
    if possible_side * 4 != perimeter:
        return False
```