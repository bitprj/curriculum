This is similar to updating documents as there is functions deleteOne and deleteMany.

In this example, we will delete people who are ages 27 in a list from the database. 

Say the list is like this:

![Screen Shot 2019-12-18 at 8.45.04 PM](/Users/jiaxianjuliama/Desktop/Screen Shot 2019-12-18 at 8.45.04 PM.png)

The code is:

	const db = client.db(databaseName)
	
	db.collection('users').deleteMany({
		age: 27
	}).then((result) => {
		console.log(result)
	}).catch((error) => {
		console.log(error)
	})

The result should look like this:

![Screen Shot 2019-12-18 at 8.45.19 PM](/Users/jiaxianjuliama/Desktop/Screen Shot 2019-12-18 at 8.45.19 PM.png)

