<!--title={Matchsticks to Square: DFS Algorithm Base Cases}-->

Now that we have established our variables and base cases, let's move on to coding our approach:

**Depth First Search (DFS) Approach**:

It is possible that any given matchstick can be a part of any of the four sides of the resulting square, but choosing which matchstick goes to which side of the resulting square is something we need to figure out.

This means that for each matchstick in our given array, we will have four different options each, representing the side of the square or subset that this matchstick could be a part of.

Using DFS, we can try out all of four options by running through the algorithm recursively until we exhaust all of the possibilities or until we find an arrangement of our matchsticks such that they form the square.

---

Building from the code we have created so far, we will first sort the array of matchsticks in reverse order, which will allow our DFS algorithm perform recursion more efficiently, and create an additional array that will store values that represent the current length of the sides of the square.    

```python
	nums.sort(reverse=True)
	sums = [0 for _ in range(4)]
```
Now, we will start building our DFS algorithm, by creating a nested function called `dfs()` for our function `makesquare()`. Let's start by allowing the parameter of `dfs()` take the current matchstick index we will process. 

Then, we will create the **base case** for the recursion process within our `dfs()` function by checking if we have already met the end of the matchsticks input array, and if so, we will check if the square has been formed of not. If three equal sides were formed, the fourth side will be the same length as these three, leading to `True` in this case.

```python
	def dfs(index):
		if index == L:
			return sums[0] == sums[1] == sums[2] == possible_side
```