<!--title={Writing a Promise}-->

<!--badges={Web Development: }-->

Here are the steps to making a promise:

1) Make a new promise

Example:
	const doWorkPromise = new Promise((resolve, reject) => {
	)}

2) Set the time you want the program to run for before the result/error prints.

Example:
	const doWorkPromise = new Promise((resolve, reject) => {
		setTimeout(() => {
		}, 2000)
	)}

3) Add your resolve or reject. 

Example:
	const doWorkPromise = new Promise((resolve, reject) => {
		setTimeout(() => {
			//resolve(17, 4, 11)
			reject('Things went wrong!')
		}, 2000)
	)}

4) Use a 'then-catch' to run the promise and catch errors if there is any.

Example:
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