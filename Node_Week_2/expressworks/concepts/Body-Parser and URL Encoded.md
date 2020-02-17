### Body-Parser and URL Encoded

`Body-parser` is a parsing middleware package that is built into Express.js so like all packages they must be installed before use. 

```
npm install body-parser --save
```

After installation you can use the body-parser object in your code

```js
var bodyParser = require('body-parser')
```

`body-parser` has many different middleware options for different formats but we will be focusing on `urlencoded`. URL encoded is the way your request is formatted. Generally speaking the format of a URL encoded resquest is a string of the names and vaules of your request where the names are attached to the values with an `=` sign and each variable is sperated with `&`. A general form of a URL encoded request would look like this `url/name1=value1&name2=value2`.

When we use `body-parser` we have to specify which format is being taken into the middleware. Since we are using `urlencoded` we would specify this and our general call to `body-parser` would look like this 

```js
bodyParser.urlencoded([options])
```

The options are paramaters that can be passed to `body-parser` that do additional tasks. An important option is the `extended` option. `extended` determines where the URL encoded data is parsed. When extended is set to true, the request is parsed in the **qs** library and returns key-value pairs of any type. When extended is set to false, the request is parsed in the **querystring** library and returns key-value pairs of strings or arrays. `Extended` set to a default true unless otherwise specified. 

Other options of `bodyParser.urlencoded([options])` are displayed below:

| Option         | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| inflate        | If `true`(default), deflated (compressed) bodies will be inflated. If `false`, deflated bodies are rejected. |
| limit          | Controls the maximum request body size.                      |
| parameterLimit | Controls the maximum number of parameters that are allowed in the URL-encoded data |
| type           | Determines what media type the middleware will parse         |

###  