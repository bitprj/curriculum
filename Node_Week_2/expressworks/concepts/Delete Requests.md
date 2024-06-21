<!--title={A Closer Look at Delete}-->

The DELETE method will delete data from the server. It is the **D** in **CRUD**. If we want to delete some data on the file route, we will use ``/file`` as the handle and delete it like so:

```javascript
app.delete ('/file:id', function (req, res) { 
  const movie = req.params.id;
  res.send('deleted it!')
})
```

