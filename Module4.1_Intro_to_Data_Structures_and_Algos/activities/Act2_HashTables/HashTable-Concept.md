<!--title={HashTable Concept}-->

1. A hash table is a data structure that is a common technique used to solve a variety of problems. 
It serves as a key value lookup.
What this means is that the programmer creates "keys" that link directly to a value. 
Later when looking up information, the programmer can simply lookup the "key" associated to the value they would like and quickly find the value.

2. A real life example would be the UC Davis student record system. 
Every student is assigned a Student ID number and when the UC Davis offices look up that ID number, a variety of information about the student appears.
Just by looking up a simple nine-digit number, the system is able to pull up information like a student's name, DOB, address, etc. 
In this example, the key is the ID number and the student information is the value. 

3. ### Hash functions
Hashtables require Hash functions that can be used to simplify data. Hash functions take in our Key value, and assign it an index in our HashTable. 

4. ### Collisions 
Something we need to be mindful for is collisions. When using a hash function, it is possible for two elements to generate the same key. To fix this, we must use a **Collision Method**. 

