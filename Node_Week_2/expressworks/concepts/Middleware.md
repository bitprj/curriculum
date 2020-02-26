### Middleware

Middleware is any software that connects operating systems like Linux, Windows, and MacOS to communication protocols and applications that run on it. We have already encountered middleware in the form of APIs. They help tie seperate applications together by "translating" between them and can allow clients to access high level programs without understanding the entire complexity of the program. Middleware can be used to optimize already existing applications as well as help create new ones efficiently.

With Express, middleware functions are used to execute code, change requests and response objects, and call more middleware functions. Middleware functions modify **req** and **res** objects and can streamline projects by preventing repetitive code blocks. Additionally, they can add a layer of security to your program by preventing users from accessing certian atributes of your code.  An example of Middleware is the `body-parser` module that is discussed in depth in another concept card. 

To use middleware in your program, we first have to import it like a module, we just use the `require` function and pass the name of the middleware as a parameter. To actually use the middleware we simply call the `use` function and pass any necessary parameters into it. If you want to see an example of middleware being executed it can be found with the `body-parser` concept card. 

A general format would just look like this:

```js
var name = require("middleware_name")
app.use(name())
```