<!--title={A Closer Look at PUT}-->

PUT updates and replaces data in server. It is the **U** in **CRUD**. Unlike POST, if the data already exists there (with the same file name), PUT replaces that file. If there is no file there, PUT will create one.

```javascript
app.put('/user/:id', function (req, res) { 
 const movie = req.params.id;
 res.send('put it!')
})
```

