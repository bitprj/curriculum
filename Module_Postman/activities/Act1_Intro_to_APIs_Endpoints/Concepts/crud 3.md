# CRUD

Many servers need to store data persistently. When dealing with persistent data storage, they generally need to be able to allow four basic operations to be performed.

- **C**reate data in the server
- **R**etrieve data from the server
- **U**pdate and replace existing data in the server
- **D**elete data from the server

These operations can be used in SQL (Structured Query Language), HTTP (Hypertext Transfer Protocol), RESTful API (Representational State Transfer), and DDS (Data Distribution)

| Operation        | SQL    | HTTP           | RESTful API | DDS       |
| ---------------- | ------ | -------------- | ----------- | --------- |
| Create           | Insert | Put/Post       | Post        | Write     |
| Read (Retrieve)  | Select | Get            | Get         | Read/Take |
| Update (Modify)  | Update | Put/Post/Patch | Put         | Write     |
| Delete (Destroy) | Delete | Delete         | Delete      | Dispose   |

Without these four operations, the software is not considered complete.