### Nodemon

Nodemon is an application that starts your server and restarts the server with every change you make in your program. We use it to start the local server accessed by express (`http://localhost:3000 `). Unlike Node which only runs your program once, when you run your program with Nodemon everytime you make a change in your program, it will run again making the whole process of testing your program more efficient. 

Like all third party applications we must install nodemon through console. 

```
npm install nodemon
```

Here we dont need `--save` because nodemon is a global package. To use nodemon it is just like justing node. When we want to run ur program we just type 

```
nodemon file.js
```

After you run the program, just head to server on a web browser and see your result!