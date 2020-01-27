<!--title={Query Strings/Parameters}-->

# Query Strings/Parameters

A simple URL with a query string might look like:

```irb
http://www.example.com?search=ruby&results=10
```

Let's take that apart:

| Query String Component | Description                                                  |
| :--------------------- | :----------------------------------------------------------- |
| ?                      | This is a reserved character that marks the start of the query string |
| search=ruby            | This is a parameter name/value pair.                         |
| &                      | This is a reserved character, used when adding more parameters to the query string. |
| results=10             | This is also a parameter name/value pair.                    |

Now let's take a look at an example. Suppose we had the following URL:

```irb
http://www.phoneshop.com?product=iphone&size=32gb&color=white
```



![Query String Components](https://d186loudes4jlv.cloudfront.net/http/images/query_string_components.png)



In the above example, name/value pairs in the form of `product=iphone`, `size=32gb` and `color=white` are passed to the server from the URL. This is asking the `www.phoneshop.com` server to narrow down on a product `iphone`, size `32gb` and color `white`. How the server uses these parameters is up to the server side application.

Another common place where you may have seen query parameters in action is when you perform a search in any modern search engine. **Because query strings are passed in through the URL, they are only used in HTTP GET requests.** We'll talk about the different HTTP requests later in the book, but for now just know that whenever you type in a URL into the address bar of your browser, you're issuing HTTP GET requests. Most links are also HTTP GET requests, though there are some minor exceptions.



![Query Strings](https://d186loudes4jlv.cloudfront.net/http/images/query_strings.jpg)



Query strings are great to pass in additional information to the server, however, there are some limits to the use of query strings:

- Query strings have a maximum length. Therefore, if you have a lot of data to pass on, you will not be able to do so with query strings.
- The name/value pairs used in query strings are visible in the URL. For this reason, passing sensitive information like username or password to the server in this manner is not recommended.
- Space and special characters like `&` cannot be used with query strings. They must be URL encoded, which we'll talk about next.