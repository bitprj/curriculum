<!--title={A Closer Look at POST}-->

The POST method can be used to send large amounts of information to a specified resource.

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

Now, we can use post like so:

```js
app.post('/', function (req, res) { // The '/'is the handler to the root route
  //code to perform any specified action
   res.send('posted!')
})
```





