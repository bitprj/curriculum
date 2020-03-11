<!--title={A Closer Look at POST}-->

POST creates data in server and is the **C** in **CRUD**.

To use post, first install **bodyParser** in the package file:

```
sudo npm install --save body-parser
```

Next, tell Express to use bodyParser as middle-ware:

```js
var express     =     require("express");
var bodyParser   =     require("body-parser");
var app       =     express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
```

Now, we can use post! Lets say we want to create some data on a server every time someone visits the homepage of our website. We would use a **post** request with ``/home`` as the handle:

```js
app.post('/home:id', function (req, res) { 
  const movie = req.params.id;
  res.send('posted!')
})
```





