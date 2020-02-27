# Hash Tables - Double Hashing

### Motivation

In Hash Tables, when there is a collision, we must have a collision resolution technique when keys are hashed to the same bucket. Double Hashing is an example of a collision resolution technique. This technique is a part of open addressing.

### Preliminary Information <sup>1</sup>

* There are **two** hash functions (`h1(k)` and `h2(k)`)

* The overall, complete hashing function is `h(k) = h1(k) + i * h2(k) % (size of table)` .

* `i` is initialized to 0 and incremented everytime there is a collision. This means that `h2(k)` is **only** used when there is a collision, otherwise we **only** use `h1(k)`. 

* The following are common examples of hash functions used in double hashing

  * `h1(k) = k % (size of table)`
  * `h2(k) = X - (k % X)`
    * X must be **prime** and **less than** the size of the hash table
    * We do not want `h2(k)` to equal 0 as this would mean that `h(k) = h1(k) + i * 0 = h1(k).`<sup>2</sup>

  

### Example

Double Hashing is best demonstrated through an example.

Say that we have a hash table of size 5. We will let `X = 3` as this is a prime number that is less than the size of the hash table. Let's try to insert the numbers 1, 6, and 11.

![](./Double_Hashing_Example.jpeg)

<hr> 

<sup>1</sup> Credit to https://www.geeksforgeeks.org/double-hashing/ for concepts for Preliminary Information section. See https://www.geeksforgeeks.org/double-hashing/ for futher explanation and their examples

<sup>2</sup>See https://www.youtube.com/watch?v=lDMc4hg1lUk for more detailed explanation











