You might want to update information from your database. You can use the updateOne funtion from the MongoDB library. It will let you update data like names, age, etc.

Example code:

	const updatePromise = db.collection('users').updateOne( {
			_id: new ObjectID("your ID value as a string")
	}, (
			$set: {
				name: 'the new name'
			}
	})
		
		updatePromise.then((result) => {
			console.log(result)
		}).catch((error) => {
			console.log(error)
		})		
	})

If you run this code, you will see a bunch of information but where you can check if the update was made, find the modified count line. 

If you used updateOne, you should see that the modified count is 1 if you update was made (since we only updated one thing) and 0 if it is not made. Also, refresh you database and you should see that the information is updated.

There are also many other update operators you can use like $set. You can find them by googling 'mongodb update operators'. They are used just like $set.

There is also a function updateMany. In this example, this code will change whether a chore is complete or not in the data of a list.

Example:

	db.collection('tasks').updateMany {
		completed: false
	}, {
		$set: {
			completed: true
		}
	}).then((result) => {
		console.log(result.modifiedCount)
	}).catch((error) => {
		console.log(error)
	})

This will have turned your incomplete (false) chores into completed (true chores).

completed is the category that we are updating, where false is that values we want to change, and true if the value we want to change to.

'Then' and 'catch' will take care of errors. When the program succeeds, the number of modified items will print else the error message will print.