## Tags

An HTML **tag** is a special word or letter surrounded by 2 carrot brackets (< and >). These tags are used as markers for creating HTML **elements**, which are special cues that tell the computer what you want it to do. 

Some examples of elements include paragraphs and links. If you want to section off your paragraphs, you would use the corresponding tag for the paragraph element, which is `<p>`. 

Most tags in HTML come in pairs; you would need an opening tag (like `<p>`) and a closing tag, which is the opening tag with a forward slash character before the element name (like this `</p>`). 

To create a paragraph, put all the text to be included in the paragraph between `<p>` and `</p>` tags. 

```html
<p>
    Hi! I think it's great that you're learning about HTML!
</p>
```



Some tags do not require a closing tag. `<br>` is a tag that creates a line break. 

Using the paragraph from earlier, 

```html
<p>
    Hi! I think it's great that you're learning about HTML!
</p>
```

would print out

> <p>
>     Hi! I think it's great that you're learning about HTML!
> </p>



Using the `<br>` function in between the 2 sentences splits the sentences.

```html
<p>
    Hi!<br>I think it's great that you're learning about HTML!
</p>
```

> <p>
>     Hi!<br>I think it's great that you're learning about HTML!
> </p>



There are many other tags other than `<p>` and `<br>`. These tags and their corresponding elements will be covered as you continue.