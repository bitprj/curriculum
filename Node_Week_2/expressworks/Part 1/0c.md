<!--title={Introduction to Routing}-->

As you already know, a REST API allows the http requests to carry through their routes and send back an appropriate status code.

For every route, there can be one or more handler functions that are are executed when the route is matched.

Routes have the following structure:

```javascript
app.METHOD(PATH, HANDLER)
```

- `app` is the `express` app, which is an instance of express.
- `METHOD` is the HTTP request method, always using  in lowercase.
- `PATH` is a path on the server.
- `HANDLER` is the function executed when the route is matched.

In the following examples cards, we will be exploring a some simple examples of each of the different kind of requests.

Respond to a PUT request to the `/user` route:

```javascript
app.put('/user', function (req, res) {
  res.send('Got a PUT request at /user')
})
```

Respond to a DELETE request to the `/user` route:

```javascript
app.delete('/user', function (req, res) {
  res.send('Got a DELETE request at /user')
})
```