## Function

A **function** is a block of code that ***1. takes input***, ***2. processes that input***, and then ***3. produces output***.

Here is an example:

```js
function example (x) {
  y = x * 2
  return y
}
```

*Name* of function: **example**

*Input* (*argument*): **x**

*processes*: **x*2**

*output* (*return value*): **y**

*****

We can ***call*** that function like this :

```js
example(5)
```

The **result** is :

```js
10
```

The above example assumes that the `example` function will take a number as an argument –– as input –– and will return that number multiplied by 2.

## The challenge:

Create a file named `functions.js`.

In that file, define a function named `eat` that takes an argument named `food`
that is expected to be a string.

Inside the function return the `food` argument like this:

```js
return food + ' tasted really good.'
```

Inside of the parentheses of `console.log()`, call the `eat()` function with the string `bananas` as the argument.

Check to see if your program is correct by running this command:

```bash
javascripting verify functions.js
```
