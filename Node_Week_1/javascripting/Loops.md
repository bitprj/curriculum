# Loops

Loops can execute a block of code a number of times.

Loops are handy, if you want to run the same code over and over again, each time with a different value.

***

#### Different Kinds of Loops

JavaScript supports different kinds of loops:

- `for` - loops through a block of code a number of times
- `for/in` - loops through the properties of an object
- `for/of` - loops through the values of an iterable object 
- `while` - loops through a block of code while a specified condition is true
- `do/while` - also loops through a block of code while a specified condition is true

***

## For Loop

The `for` loop has the following syntax:

```javascript
for (statement 1; statement 2; statement 3) {
 // code block to be executed
}
```

**Statement 1** is executed (one time) before the execution of the code block.

**Statement 2** defines the condition for executing the code block.

**Statement 3** is executed (every time) after the code block has been executed.

**Example:**

```javascript
for (i = 0; i < 5; i++) {
 text += "The number is " + i + "<br>";
}
```

**Result:**

```javascript
The number is 0
The number is 1
The number is 2
The number is 3
The number is 4
```

#### Statement 1

Normally you will use **statement 1** to initialize the variable used in the loop (i = 0).

This is not always the case, JavaScript doesn't care. Statement 1 is optional.

You can **initiate many values** in statement 1 (separated by comma):

```javascript
var cars = ["BMW", "Volvo", "Saab", "Ford"];
var i, len, text;
for (i = 0, len = cars.length, text = ""; i < len; i++) { 
 text += cars[i] + "<br>";
}
```

**Result:**

```javascript
BMW
Volvo
Saab
Ford
```

And you can **omit statement 1** (like when your values are set before the loop starts).

#### Statement 2

Often statement 2 is used to **evaluate the condition** of the initial variable.

If **statement 2 returns <u>true</u>**, the **loop** will <u>**start over again**</u>, if it returns **<u>false</u>**, the loop will **<u>end</u>**.

#### Statement 3

Often statement 3 **increments** the value of the **initial variable.**

Statement 3 can do anything like **negative increment** (`i--`), **positive increment** (`i = i + 15`), or anything else.

## While Loop

The `while` loop loops through a block of code as long as a specified condition is true.

**Syntax**:

```javascript
while (condition) {
 // code block to be executed
}
```

**Example**:

In the following example, the code in the loop will run, over and over again, as long as a variable (i) is less than 10:

```javascript
while (i < 10) {
 text += "The number is " + i;
 i++;
}
```

**Result:**

```javascript
The number is 0
The number is 1
The number is 2
The number is 3
The number is 4
The number is 5
The number is 6
The number is 7
The number is 8
The number is 9
```