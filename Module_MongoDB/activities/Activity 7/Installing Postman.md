<!--title={Installing Postman}-->

# Installing Postman

First, head over the https://www.getpostman.com/ to installing Postman.

After installed, we can use postman to fire off an HTTP request for the Weather app we preivously wrote before. If it works, then we will know the tool is set up correctly.

###Sending your first request

An API request lets you contact a server with API endpoints that you want to reach and perform some action. Those actions are HTTP methods.The most common methods are GET, POST, PUT, and DELETE. The names of the methods are self-explanatory. 

GET enables you to retrieve data from a server. 

POST enables you to add data to an existing file or resource in a server. 

PUT lets you replace an existing file or resource in a server. 

DELETE lets you delete data from a server.

Postman makes sending API requests simple. Instead of testing your APIs through a command line or terminal, it offers an intuitive graphical interface that is quick to learn and rewarding to master. As you can see in the image below, when you enter a request in Postman and click the **Send** button, the server receives your request and returns a response that Postman displays in the interface.![request and response illustration](https://assets.postman.com/postman-docs/anatomy-of-a-request.png)Sending a requestNow, let's send our first API request! Enter `https://mead-weather-application.herokuapp.com/wether` into the URL field. Then, we need to provide an address for it. in the key and value box below, type address and boston respectively. Now click the **Send** button to send your request. Note the JSON data response from the server

![](https://tva1.sinaimg.cn/large/006tNbRwgy1ga0wwp2x8uj31hv0u04mz.jpg)

 You can click the **Save** button to save a request to use later.

![postman echo example](https://assets.postman.com/postman-docs/SaveRequest.png)