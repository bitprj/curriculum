# Arrays

JavaScript arrays are used to store multiple values in a single variable.

#### What is an Array?

An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example) below:

```javascript
var car1 = "Saab";
var car2 = "Volvo";
var car3 = "BMW";
```

So now you have 3 different variables, it will be diffcult for you to find a specific one of you have 300 different variables.

**BUT Array** can help you !!

An array can hold many values under a single name, and you can access the values by referring to an index number.

***

## Creating an Array

There are three ways to create an array. All of them are okey.
The following code defines an array object called **myCars**:

1. ```javascript
   var myCars=new Array(); 
   myCars[0]="Saab";       
   myCars[1]="Volvo";
   myCars[2]="BMW";
   ```

2. ```javascript
   var myCars=new Array("Saab","Volvo","BMW");
   ```

3. ```javascript
   var myCars=["Saab","Volvo","BMW"];
   ```

***

## Access the Elements of an Array

You access an array element by referring to the **index number**.

This statement **accesses** the value of the first element in `myCars`:

```javascript
var name=myCars[0];
```

The **result** in *name* will be:

```javascript
"Saab"
```

This statement **changes** the value of the first element in `myCars`:

```javascript
myCars[0]="Opel";
```

The **result** of array `myCars` will be:

```javascript
["Opel","Volvo","BMW"]
```

***

## Adding Array Elements

The easiest way to add a new element to an array is using the `push()` method:

```java
myCars.push("Audi")
```

The **result** of array `myCars` (which already change the first element above)will be:

```javascript
["Opel","Volvo","BMW","Audi"]
```

***

## Array Elements Can Be Objects

JavaScript variables can be objects. Arrays are special kinds of objects.

Because of this, you can have variables of **different types** in the same Array.

You can have objects in an Array. You can have functions in an Array. You can have arrays in an Array:

```javascript
myArray[0] = Date.now; //objects
myArray[1] = myFunction; //functions
myArray[2] = myCars; //array
```