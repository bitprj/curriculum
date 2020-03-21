## Unordered Lists

One of the ways to represent a list of items is an unordered list, which displays items without numerical ordering. It is equivalent to a bulleted list that can be created in Word or any word processor.

The HTML `<ul>` tag is used to specify an unordered list. All the information about the list will go in between the `<ul>` opening tag and `</ul>` closing tag. 

```html
<ul>
    Contents of the list go here!
</ul>
```



Each list element is contained within a list item tag (`<li>`) pair. Let's say we're making a shopping list. To add "eggs" and "milk" to a list, you would surround each word in `<li>` and `</li>`, creating a new `<li>` tag pair for each list item. 

```html
<ul>
    <li>eggs</li>
    <li>milk</li>
</ul>
```



That would create a list that looks like this:

<ul>
    <li>eggs</li>
    <li>milk</li>
</ul>