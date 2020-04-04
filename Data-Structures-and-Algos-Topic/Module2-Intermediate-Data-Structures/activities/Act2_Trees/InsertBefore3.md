<!--title={Recursion}-->

<!--badges={Algorithms:5,Python:5}-->

# Recursion with Binary Search Trees 

Recursion is a common coding strategy where we write a function that calls itself until it reaches a base case. 
Below is a code example where recursion is implemented to find the factorial of a number. 
The function takes in a number and should return the factorial of the number. 
When writing a recursive function, we want to first establish a base case. In this case, the mathematical relationship of the factorial of 7 would be ...

```
7*6*5*4*3*2*1
```
It multiplies every number from 7*1 and after it multiplies by 1, all calculations are finished. Hence, our **base case** will be when number == 1. 
It may seem confusing now, but it will make sense when all the pieces come together. 

``` python
def fact(number): 
  if(number == 1) //base case 
    return product;
```
Now, let's write the rest of our recursive function. Since `number == 7` (in our example), it wouldn't fall into our if-statement. We will write an `else` statement that accounts for when `number` != 1. 
```python
  else
    product = number*(fact(number-1)) // this is where the recursion occurs
```
This is the rest of the function. We will multiply `number *fact(number-1)`. When `Fact` is called, `number` will not equal 1. 
The pseudo code will look like this: 

```
product = number*(number-1)*(fact(number-1)). 
Using our example of fact(7), the computation of our program will look like this:
`7*6*fact(number-1)`.

When fact is called again, `number` == 5, and the pattern will repeat until `number` == 1. 
Eventually the computation will look like this: 
7*6*5*4*3*2*1
Since the last `number` multiplied is 1, the base case is reached and `product` is returned. 

### Another Example
Recursion is an incredibly confusing topic, so let's take a look at another example before we implement it into our Binary Search Tree.
The general outline we want to approach recursion is:
1. Simplify the problem into something smaller. 
   - Our problem is adding `num1` to the number above it. 
2. Solve the simpler problem with an algorithm.
   - To solve our problem, we can solve it by calling our function multiple times. 
     In this case, calling the same function with a `num1+1`
3. Putting Everything Together 

Let's write a recursive function to find the sum of an interval of numbers. We will want two inputs and every number between those inputs will be added.
​```python
def interval(num1, num2):
```
First, let's write our base case. If `num1 == num2`, then that means the interval is zero and there are no more numbers to add. So, our base case looks like this:
Sum is simply the number that is the sum of the interval of numbers.

```python
if (num1 == num2)
  return sum
```

Now, let's incorporate our logic. In our else-statement, we want to call the same function, but with `num1+1` as our input. 
```python
else
  sum = num1 + interval(num1+1, num2)
```
Eventually, after enough calls, num1 will equal num2 and our function will return sum. 

Recursion has an incredible wide use of applications that we can implement and look further into. 

