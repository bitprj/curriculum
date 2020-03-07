<!--title={URL Parameters}-->

A **URL Parameter** is a value in the header of a url of the format `url/parameter`. URL Parameters can be passed into the URL in a couple of ways. 



Let's say for example, that there's a website *fakebook*, that has a profile page of someone named Jake. The url to access his profile page might look like `fakebok/profile_page/:jakeid`. This way of passing something into the URL only passed one value to the web server. 



The passing of parameters into a URL allows users to dynamically display pages. In other words, URL parameters open up possibilities for different pages to be displayed. Considering the *Fakebook* example, how would the web server know a user was trying to access a certain profile page if we didn't somehow tell the web server? 



Another way a parameter can be passed is through the `?`. Items can be passed into URLs in other forms than what we did previously, like `/url/:value`. Another way to pass items into the URL is in a **key** and **value** pair. The format to do so would be `/route?key1=value1`. If we wanted to get multiple keys and pairs, you could add an `&`in the URL. Here's an example format: 

```
/route?key1=value1&key2=value2
```

Potentially we can add as many key and value pairs as we want. In this exercise, we'll write a route that extracts data from the query string in the GET `/search` URL form `?results=recent&include_tabs=true` and then outputs it back to the user in JSON format.