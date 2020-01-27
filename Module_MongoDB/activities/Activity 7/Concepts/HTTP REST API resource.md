<!--title={HTTP REST API resource}-->

# HTTP REST API resource

The fundamental concept in any RESTful API is the *resource*. A resource is an object with a type, associated data, relationships to other resources, and a set of methods that operate on it. It is similar to an object instance in an object-oriented programming language, with the important difference that only a few standard methods are defined for the resource (corresponding to the standard HTTP GET, POST, PUT and DELETE methods), while an object instance typically has many methods.

Resources can be grouped into *collections*. Each collection is homogeneous so that it contains only one type of resource, and unordered. Resources can also exist outside any collection. In this case, we refer to these resources as *singleton resources*. Collections are themselves resources as well.

Collections can exist globally, at the top level of an API, but can also be contained inside a single resource. In the latter case, we refer to these collections as *sub-collections*. Sub-collections are usually used to express some kind of “contained in” relationship. We go into more detail on this in Relationships.

The diagram below illustrates the key concepts in a RESTful API.

![_images/concepts.png](https://restful-api-design.readthedocs.io/en/latest/_images/concepts.png)

We call information that describes available resources types, their behavior, and their relationships the *resource model* of an API. The resource model can be viewed as the RESTful mapping of the application data model.