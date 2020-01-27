<!--title={REST API}-->

# REST API

###What is a REST API?

**API** stands for Application programming interfac. It is a set of rules that allow programs to talk to each other. The developer creates the API on the server and allows the client to talk to it.

**REST** determines what the API looks like. It stands for “Representational State Transfer”. Its architectures consist of clients and servers. Clients initiate requests to servers; servers process requests and return appropriate responses. Requests and responses are built around the transfer of representations of resources. It is also a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called a resource) when you link to a specific URL.

Each URL is called a **request** while the data sent back to you is called a **response**.

###What is REST API for?

Using **REST API** would allow you to develop any kind of web application having all possible CRUD (create, retrieve, update, delete) operations. REST guidelines suggest using a specific HTTP method on a specific type of call made to the server. This leads to HTTP Request.

###HTTP Request

**HTTP requests** are messages sent by the client to initiate an action on the server. Their *start-line* contain three elements:

1. An *[HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)*, a verb (like [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET), [`PUT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) or [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)) or a noun (like [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) or [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS)), that describes the action to be performed. For example, `GET` indicates that a resource should be fetched or `POST` means that data is pushed to the server (creating or modifying a resource, or generating a temporary document to send back).

2. The request target, usually a URL, or the absolute path of the protocol, port, and domain are usually characterized by the request context. The format of this request target varies between different HTTP methods. It can be

- An absolute path, ultimately followed by a `'?'` and query string. This is the most common form, known as the *origin form*, and is used with `GET`, `POST`, `HEAD`, and `OPTIONS` methods.
  `POST / HTTP/1.1GET /background.png HTTP/1.0HEAD /test.html?query=alibaba HTTP/1.1OPTIONS /anypage.html HTTP/1.0`

- A complete URL, known as the *absolute form*, is mostly used with `GET` when connected to a proxy.
  `GET http://developer.mozilla.org/en-US/docs/Web/HTTP/Messages HTTP/1.1`
- The authority component of a URL, consisting of the domain name and optionally the port (prefixed by a `':'`), is called the *authority form*. It is only used with `CONNECT` when setting up an HTTP tunnel.
  `CONNECT developer.mozilla.org:80 HTTP/1.1`
- The *asterisk form*, a simple asterisk (`'*'`) is used with `OPTIONS`, representing the server as a whole.
  `OPTIONS * HTTP/1.1`

3. The *HTTP version*, which defines the structure of the remaining message, acting as an indicator of the expected version to use for the response.

### Basic Structure for HTTP REST API resource

| Operation        | SQL    | HTTP/REST |
| :--------------- | :----- | :-------- |
| Create           | INSERT | POST      |
| Read (Retrieve)  | SELECT | GET       |
| Update           | UPDATE | PUT       |
| Delete (Destroy) | DELETE | DELETE    |

These actions depend on the resource that has been identified and we have defined 5 standard cases of interaction.

| Command (HTTP CODE) | CRUD Operation   | Resource Identified                                 | Description                                                  |
| :------------------ | :--------------- | :-------------------------------------------------- | :----------------------------------------------------------- |
| index (GET)         | Read (Retrieve)  | Collection URI (`http://example.com/resources/`)    | List the URIs and perhaps other details of the collection's members. |
| get (GET)           | Read (Retrieve)  | Element URI (`http://example.com/resources/item17`) | Retrieve a representation of the addressed member of the collection, expressed in an appropriate Internet media type. |
| post (POST)         | Create           | Collection URI (`http://example.com/resources/`)    | Create a new entry in the collection. The new entry's URL is assigned automatically and is usually returned by the operation. |
| put (PUT)           | Update           | Element URI (`http://example.com/resources/item17`) | Replace the addressed member of the collection, or if it doesn't exist, create it. |
| delete (DELETE)     | Delete (Destroy) | Element URI (`http://example.com/resources/item17`) | Delete the addressed member of the collection.               |

