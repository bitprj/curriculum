A promise is verys similar to a call back except there will be less room for error and easier to understand. 

Here's a visual of how a promise works.

​													fulfilled
​												/
​	Promise ---> pending -->
​												\
​													rejected

When a task is sent in, it's either going to be fulfllied (resolve) or rejected (reject). 

In a call backs, the first arguement will be retianed if something failed and the second arguement will be returned if something succeeded. On the other hand, in promises, resolve runs when when the work is successful while reject runs when there is an error.

The adavantage of having promises over callbacks is that you'll actually know if something failed or not. You can easier parse the code and find out what's actually going on. By having recolve and reject seperate, once one succeeds, the program stops and won't run the others.

Also, in a call back, it will be up to us the developers to decide if there is an error or not. A promise does a catch where the result will print if things are good and the error message will print if things go wrong.

A callback will go like this:

	const doWorkCallBack = (callback) => {
		setTime(() => {
			//callback('This is my error!', undefined)
			callback(undefined, [1, 4, 7])
		}, 2000)	
	}
	
	doWorkCallBack((error, result) => {
		if (error) {
			return console.log(error)
		}
		console.log(result)
	})

While a promise will look like this:

	const doWorkPromise = new Promise((resolve, reject) => {
		setTimeout(() => {
			//resolve(17, 4, 11)
			reject('Things went wrong!')
		}, 2000)
	)}
	
	doWorkPromise.then((result) => {
		console.log('Success!', result)
	}).catch((error) => {
		console.log('Error!', error)
	})

Resolve and reject both takes one optional argument, the message for error or success. 

Reject takes the first arguement from the callback function.
Resolve takes the takes the second arguement from the callback function.



