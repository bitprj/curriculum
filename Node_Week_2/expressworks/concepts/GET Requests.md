<!--title={A Closer Look at GET}-->

GET requests retrieve data from server. It is the **Read** of the **R** in **CRUD**.

Lets say we want to retrieve some data from a server every time someone visits the homepage of our website. We would use a **get** request with ``/home`` as the handle:

```javascript
app.get('/home', function (req, res) {
   //code to perform a specified action
})
```

Lets say that on the home page, we have some information that we would like to retreive. In the home.html file, it contains:

```html
<html>  
<body>  
<form action="/home" method="GET">  
Favorite Movie: <input type="text" movie="movie_name"/>  <br/>  
<input type="submit" value="Submit"/>  
</form>  
</body>  
</html>  
```

Now, when we use the **get** request, we can use data from the server to perform an action:

```javascript
app.get('/home', function (req, res) {
 res.send('<p>Favorite Movie: ' + req.query['movie']'</p>');  
})  
```

Lets say instead you want to get all of your favorite movies of a page called ``fav_movies``:

```js
app.get('/fav_movie:movies', function (req, res) {
   //TODO: add in another use-case
})  


```

![An example GET request on Github](https://res.cloudinary.com/indysigner/image/fetch/f_auto,q_auto/w_400/https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/b6d1a8b7-51ef-45d2-a416-b34d7c76abda/understanding-api-doc-github-repo-get-opt.png)