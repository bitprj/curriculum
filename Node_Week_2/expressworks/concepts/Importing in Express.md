### Installing and Importing Modules 

Node.js has 3 different types of modules that can be accessed through your code. Built-in modules do not need to be installed and can be used just by importing them into your code. NPM Modules are thrid party modules that can be installed into a `node_modules` folder through the terminal and accessed with Node.js. Express is an example of a NPM module. Lastly there are local modules that are accessed by providing a file path to your module. These are in the form `./`,`/`,or`../`.

To access these modules in our code we have to import them. We normally do this with `require('module_name')`. The parameter passed into `require()` is the nam e of the module you are trying to import. Here's what it looks like to import Express into our code 

```js
var express = require('express')
```

Breaking this line down, `var` is used as standard JS syntax for a variable, `express` is the name we assign the variable that contains the express module, and we use `require()` to import the module `express`. 

Some important files that you should be familiar with are `package.json` and `package-lock.json` files. Both serve a similar goal: To keep track of the exact version of every package that is installed so that the project is updateable when packages are updated too. A `package.json` file is part of all nmp packages and stores all the metadata (data about the data) of the project, like version, description, licensing, ect. . It gives information to npm to help with identification and project dependencies.

Even though there is a lot of information in the `package.js` file, Node only accesses 2, name and version, where name  is the name of the project and version is the version of the package installed.  Version will appear like this:

```json
"version" = "#.#.#"
```

where each hastag is an integer representing major, minor, patch respectively. Using semver notation you can auto-update versions.  A `~` before the version number means you only want to update patch releases,  and a `^` before the version number means you only want to udpate patch and minor releases.

Other meta properties found in `package.js` include:

| Meta Properties |                                                              |
| --------------- | ------------------------------------------------------------ |
| description     | a quick description of the project                           |
| keywords        | tags that identify the project                               |
| main            | main entry point for library                                 |
| dependencies    | lists modules that the project depends on, installs them when project is installed through nmp |

`package-lock.json` is very similar to `package.json`, the change is that instead of alllowing for updating versions of a  package that could potentially introduce bugs into your code, `package-lock.json` "locks" the installed version number for the project such that when other users download and run it there should be no issues with version numbers. You can still update your dependencies by running `npm udpate`.