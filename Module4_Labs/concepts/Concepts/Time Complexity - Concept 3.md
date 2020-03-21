<!--title={Time Complexity}-->

# Time Complexity

Time Complexity boils down to the rate the runtime of a function increases as the input gets very large. 

Functions and algorithms can increase in a variety of different "times" and its important to know what each time represents. 

To determine the time function grows in, we look at each individual line and approximate how the increase in runtime as input increases. 

## Looking at a function

``` python
class_grade = [80, 73, 20, 45, 100]
def GradeAverage(class_grade):

    average = 0
    count = 0
    for i in class_grade:
        average = average + i
        count = count + 1
    average = average / count

    return average

```

To calculate the time, break the code by lines.

```python
average = 0     
count = 0
```

Both these lines will take a constant amount of time: *c~1~* and *c~2~* respectively. 

```python
average = average + i
count = count + 1
```

These lines also take a constant amount of time: *c~3~* and *c~4~* respectively. However, they repeat *n* amount of times so the runtime of these lines would be *n* * *c~3~* and *n* * *c~4~*. 

``` python
average = average / count 
return average
```

 These lines take a constant amount of time *c~5~* and *c~6~*. 

When looking for time complexity, the fastest growing term determines the time the function grows in. For our function `AverageGrade` , it would run in linear time because the runtime of a function increases as n increases. 

### Big - O Notation

We use Big-O notation to express the time a function grows in. 

* A function that grows in a *constant time* doesn't grow at all. A graph of its runtime vs input size would be a straight, constant line. 
* Growing in *Linear Time* means that the function of runtime vs input size increases at a steady rate. This means as the input size increases, the runtime increases at a constant rate. 
* Growing in *Quadratic Time* would mean that the graph of the function's runtime vs its input size would look like the graph of a quadratic function. This means that as the input size increases, the runtime increases at a faster and faster rate, unlike growing in *Linear time*.

| Time             | Big-O Notation |
| ---------------- | -------------- |
| Constant Time    | O(1)           |
| Logarithmic Time | O(log n)       |
| Linear Time      | O(n)           |
| Quadratic Time   | O(n^2^))       |
| Factorial Time   | O(n!)          |

Time Complexity is very important when it comes to functions because it allows us to measure how fast a function will grow. Its important to understand what each specific time represents and which time is faster than others (the chart above goes from fastest to slowest from top to bottom) as it allows us to understand the speed with which our function performs as input size gets very large. Ideally, we would like our functions to be as fast as possible and we can only understand relative by speed by recognizing the different time complexities!

**Time Complexity does not tell us the runtime of a function!! Calculating the runtime of a function is much harder because we have to consider hardware, IDE, etc**.

