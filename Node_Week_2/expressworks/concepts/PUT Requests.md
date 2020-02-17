<!--title={A Closer Look at PUT}-->

PUT also sends data to a resource. Unlike POST, if the data already exists there (with the same file name), PUT replaces that file. If there is no file there, PUT will create one.

```javascript
app.put('/user', function (req, res) { // PUT request to the 'user' route
  res.send('put it!')
})
```

