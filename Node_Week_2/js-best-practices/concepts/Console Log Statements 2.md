<!--title={Console.log()}--> 

Debugging with `Console.log()` in JavaScript is equivalent to using the `print` statement in other languages.



Documentation defines `console.log()` as: 

*Prints to stdout with newline. This function can take multiple arguments in a `printf()`-like way.* 

```javascript
console.log('count: %d', count);
```

The above line would print to std out `count: 6` (assuming count=6). 

Note: `Console.log()` is the same as `Console.info()` and `Console.debug()`



One of the most efficient ways to debug using `Console.log()` is to use the statements as often as possible and before and after blocks/lines of code. Consider the following example that is supposed add 6 to count, but has an error: 

```javascript
function count(req, res) {
	var count = 0;
  
  console.log(count);
  
	count = count + 14;
  
  console.log(count);
}
```

The terminal output is: 

```
0
14
```

`Console.log()` statements are useful this way to understand values of variables and where errors are. 