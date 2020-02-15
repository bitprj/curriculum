# JavaScript Function

A JavaScript function is a block of code designed to perform a particular task which will be executed when "something" calls it.

#### Why Functions?

You can **reuse** code. (Define the code once, and use it many times)

You can use the same code many times with different arguments, to produce different results.

***

### JavaScript Function Syntax

***1）keyword function, 2)  function name, 3)  parameter, 4)  code***

1. A JavaScript function is defined with the `function` keyword, followed by a **name**, followed by parentheses **()**.
2. **Function names** can contain <u>*letters, digits, underscores*</u> and <u>*dollar signs*</u> .
3. The parentheses may include parameter names separated by commas:
   **(parameter1, parameter2, ...)**
4. The code to be executed, by the function, is placed inside curly brackets: **{}**

```javascript
function name(parameter1, parameter2, parameter3) {
  // code to be executed
}
```

***

### Function Return

Sometimes we want the function to **return the value where it was called**. This can be achieved by using a **`return`** statement.

When JavaScript reaches a **`return`** statement, the function will stop executing.

Functions often compute a **return value**. The return value is "returned" back to the "caller".

**Example:**

```javascript
var x = myFunction(4, 3);   // Function is called, return value will end up in x

function myFunction(a, b) {
  return a * b;             // Function returns the product of a and b
}
```

The **result** in **x** will be:

```javascript
12
```

You can also use a return statement when you just want to exit a function. The return value is optional, like this example below.

```javascript
function myFunction(a,b) {
  if (a>b)    
  {        
    return;
  }    
   x=a+b 
}
```

If a is greater than b, the above code exits the function and does not calculate the sum of a and b **without return value**.

***

### Variables

**Local Variables**

Variables declared within a JavaScript function（use `var`）, become **LOCAL** to the function.

***Local variables*** can only be accessed from <u>***within the function***</u>.

**Global Variables**

Variables declared <u>***outside the function***</u> are **global variables** and are **accessible** to <u>***all scripts and functions on the web page***</u>.

**Example:**

```javascript
// code here can NOT use carName, can use carName2
carName2 = 'Happy';//(Global Variables)

function myFunction() {
 var carName = "Volvo"; //(Local Variables)
 // code here CAN use carName, can use carName2
}

// code here can NOT use carName, can use carName2
```