<!--title={A Closer Look at Delete}-->

The DELETE method will delete some data or file from the server side.

```javascript
app.delete ('/file', function (req, res) { // DELETE request to the 'file' route
  res.send('deleted it!')
})
```

