<!--title={URL Components}-->

# URL Components

When you see a URL, such as "http://www.example.com:88/home?item=book", it's comprised of several components. We can break this URL into 5 parts:

- `http`: The **scheme**. It always comes before the colon and two forward slashes and tells the web client how to access the resource. In this case it tells the web client to use the Hypertext Transfer Protocol or HTTP to make a request. Other popular URL schemes are `ftp`, `mailto` or `git`.
- `www.example.com`: The **host**. It tells the client where the resource is hosted or located.
- `:88` : The **port** or port number. It is only required if you want to use a port other than the default.
- `/home/`: The **path**. It shows what local resource is being requested. This part of the URL is optional.
- `?item=book` : The **query string**, which is made up of **query parameters**. It is used to send data to the server. This part of the URL is also optional.



![URL Components](https://d186loudes4jlv.cloudfront.net/http/images/url_components.png)



Sometimes, the path can point to a specific resource on the host. For instance, [www.example.com/home/index.html](http://www.example.com/home/index.html) points to an HTML file located on the example.com server.

Sometimes, we may want to include a port number which the host uses to listen to HTTP requests. A URL in the form of: http://localhost:3000/profile is using the port number `3000` to listen to HTTP requests. The default port number for HTTP is port `80`. Even though this port number is not always specified, it's assumed to be part of every URL. **Unless a different port number is specified, port `80` will be used by default in normal HTTP requests.** To use anything other than the default, one has to specify it in the URL.