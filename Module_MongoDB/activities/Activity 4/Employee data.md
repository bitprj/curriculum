<!--title={Employee Data}-->

<!--badges={Web Development: }-->

Say you run a corner store and you have 5 employees. You keep their basic information in a list like such:

![](https://projectbit.s3-us-west-1.amazonaws.com/darlene/labs/Screen+Shot+2019-12-20+at+3.16.30+PM.png)

What if you want to update Gunther's name to Jack because he got sick the name of Gunther? You can use updateOne from the MongoDB library!

You want to go into your database (using a platform such as Robot3T, which this example is based off of). Then you want to right click the document you want to update and choose "Edit Document" or the equivalent in your database.

You will recieve all the information of that document in a JSON format. Copy the ID.

Start by doing this:

```js
const db = client.db(databaseName)

const updatePromise = db.collection('users').updateOne( {
		_id: new ObjectID("copied ID value as a string")
}
```

The ID you copied goes in the "copied ID value as a string".
This will give the program access to the information to the data of that employee.

Next add to the code the following :

```js
const updatePromise = db.collection('users').updateOne( {
	 	_id: new ObjectID("copied ID value as a string")
}, (
	 $set: {
		 name: 'the new name'
	 }
})		
```

This will help you use the $set function to set the name of an employee to something new, in this case Jack.

Finally add:		

```js
updatePromise.then((result) => {
	console.log(result)
}).catch((error) => {
	console.log(error)
})		
```

to run the update promise you made. 

This will take care of errors. When the program succeeds, the number of modified items will print, otherwise the error message will print.

What if Jen stopped working at the store? Well, you would want to delete her from the employee list by using deleteOne!

Type the following code:

```js
const db = client.db(databaseName)

db.collection('users').deleteOne({
	name:Jen
}).then((result) => {
	console.log(result)
}).catch((error) => {
	console.log(error)
})
```
As you can see, everything is similar to updateOne except you don't have to use any $-sign functions.

And your updated employee list should look like this:

![](https://projectbit.s3-us-west-1.amazonaws.com/darlene/labs/Screen+Shot+2019-12-20+at+3.16.37+PM.png)