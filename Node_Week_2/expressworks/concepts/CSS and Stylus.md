### CSS

CSS, also known as Cascading Style Sheets, is a language used to style HTML. It controls the design and layout of a web page and helps simplify standard HTML by removing formatting. 

We will not be using standard CSS in our programs. 

### Stylus middleware

Stylus is a CSS-preprocessor built into Node.js. This means that Stylus complies into CSS for use. To access Stylus from node we first have to install the package through our console with

```
npm install stylus --save
```

The general syntax accessing Stylus from Express.js is  

```js
app.use(require('stylus').middleware('path'));
```

where the parameter passed to middleware is the path to the stylus files. 

To write in Stylus, create a new file and save it with the `.styl` file extension.

In the `.styl` file is where we write our Stylus code. The syntax is very lax when writing in Stylus so there are not many conventions that need to be followed. You can follow basic indentation like in Python or write in standard CSS code. However, you do not need brackets, colons, or semi-colons. Basically, your code would work if you wrote it like this

```stylus
p
	color red 
```

or this 

```stylus
p{
 color: red;
}
```

since they would both compile to

```stylus
p {
  color: #f00;
}
```

Some other things you can edit with Stylus include font, font size, width, height, and margins. Feel free to explore with a Stylus file and just see what works best for you!

