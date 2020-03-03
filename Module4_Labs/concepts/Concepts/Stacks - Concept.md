<!--title={Stack General Info}-->

# Stacks

## introduction

**Stack** is a linear data structure which follows a particular order in which the operations are performed. 

Stack is a very important data structure in Python. It is essentially a list of elements in Python that we can use to work with data. It is a linear data structure that has a very flexible size and is very easy to add elements to. A stack is very similar to a queue, although the fundamental difference is that the stack follows the **LIFO rule - Last in, first out**. 

You can think of a stack data structure as similar to a stack of plates. When you reach to pick up a plate, you always grab the plate on the top. Essentially, the plate that you placed last is on top and this plate is the first one you remove when you grab a plate (**L**ast **I**n **F**irst **O**ut).

As we will see, stacks are used in many algorithms and for the implementation of functions for many data structures. For example, stacks are used in graph (another important data structure) algorithms such as Depth-First Search. 

## Stack Function

Stacks, as a data structure, are essentially a class. We can create a stack with the following code here. 

```Python
class Stack():
    def __init__(self):
     self.items = []
```

if we add elements into stack, we can use `stack.push()`



if we print the stack, it will follow the LIFO and print 1,2,3,4

```python
#print
def printStack(s): 
      
    # if stack is empty then simply return 
    if s.count() == 0: 
        return
    x = s.peek() 
  
    # pop top most element of the stack 
    s.pop() 
      
    # recursively call the function printStack 
    printStack(s) 
    print("{} ".format(x), end = "") 
    s.push(x) 

#insert
if __name__=='__main__': 
    s=Stack() 
    s.push(1) 
    s.push(2) 
    s.push(3) 
    s.push(4) 
  
    printStack(s) 
```



### Things to remember:

1. The topmost element provides information about the number of elements in the stack and if the stack is full or empty. 
2. The last element to enter the stack will be the first to leave. (**Last In First Out - LIFO**). 
3. You cannot remove elements from an empty stack. 
4. Random access is not allowed.