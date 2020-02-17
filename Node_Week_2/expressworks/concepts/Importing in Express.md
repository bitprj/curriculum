### Installing and Importing Modules 

Node.js has 3 different types of modules that can be accessed through your code. Built-in modules do not need to be installed and can be used just by importing them into your code. NPM Modules are thrid party modules that can be installed into a `node_modules` folder through the terminal and accessed with Node.js. Express is an example of a NPM modlue. Lastly there are local modules that are accessed by providing a file path to your module. These are in the form `./`,`/`,or`../`.

To access these modules in our code we have to import them. We normally do this with `require('module_name')`. The parameter passed into `require()` is the nam e of the module you are trying to import. Here's what it looks like to import Express into our code 

```js
var express = require('express')
```

Breaking this line down, `var` is used as standard JS syntax for a variable, `express` is the name we assign the variable that contains the express module, and we use `require()` to import the module `express`. 