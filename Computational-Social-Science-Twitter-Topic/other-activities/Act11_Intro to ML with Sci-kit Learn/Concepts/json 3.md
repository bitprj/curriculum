

<img src="https://as2.ftcdn.net/jpg/00/54/32/71/500_F_54327132_ZNqKeHQXPhSEdUdzQFC9v46QJR3J4LUT.jpg" />

JSON stands for JavaScript Object Notation. All API data is returned in JSON format. JSON data looks a lot like a Python dictionary where you have a key on the left and a value on the right.

Example: Lets say we have the following data returned from a movie API.

    `"movies": {
        "Thor": {
            "Rating": 4,
        },
        "Spiderman": {
            "Rating": 5,
        },
        "Superman": {
            "Rating": 3,
        }
    }`

Assume that the above JSON data is stored in a variable called `movie_list`.

To get the rating data about Thor, we need to use square brackets to get specific data that we need. To get the rating on Thor we would need to do:

`movie_list["Thor"]["Rating"]` to get Thor's movie rating. `movie_list["Thor"]["Rating"]` yields a value of 4. 

If we only wanted to get Thor's object we would use:
`movie_list["Thor"]` to get the Thor object.