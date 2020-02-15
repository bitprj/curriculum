<!--title={A Closer Look at GET}-->

GET requests fetch data from specified resource. 

```javascript
app.get('handle', function (req, res) {
  //code to perform a specified action
})
```

In this case, GET is fetching the the data from the handle.

Often, the handle is simply `/` which is the root:

```javascript
app.get('/', function (req, res) {
  //code to perform a specified action
  res.send('got it!')
})
```

