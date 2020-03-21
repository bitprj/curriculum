<!--title={Space Complexity}-->

# Space Complexity

Space Complexity is the rate of a function's memory usage as input increases. As the input of functions and algorithms gets very large, the amount of memory required also will increase. It can increase in different rates and Space Complexity allows us to express those rates.

Space Complexity revolves much more on *data types* rather than executing the code. 

*Integers*, *floats*, *Strings* are **data types** that always take a constant amount of memory. 

**Data Types** like arrays do not take a constant amount of memory. The elements inside an array are malleable so the amount of memory an array takes fluctuates. 

Why does understanding the Space Complexity of a function or algorithm matter? It is important as we do not want our functions to **waste** memory space. That is, if we can solve a problem using one array of size N instead of two arrays of size N, the solution with one array would be better in terms of **space** complexity (please note that we are focusing on **space**). However, space complexity is only one aspect of analyzing an algorithm's efficiency and a minimal space usage does not *neccessarily* mean that the function is considered *efficient* as we might want to consider other factors such as time complexity as well.

## Looking at a function

```python
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

Lets examine this block of code, line by line. 

The values of the variables`Average` and `Count` will always take a constant amount of space. Those values are *c~1~* and *c~2~*. 

We have another data type, `class_grade`, which takes up *c~3~* amount of memory for every *n* element. The amount of memory this takes is *n* * *c~3~* . 

The term that has the fastest growing memory usage determines the rate of how much memory is being used by the function. In this case, it would be *n* * *c~3~* which means the function's memory usage growth is linear. 



