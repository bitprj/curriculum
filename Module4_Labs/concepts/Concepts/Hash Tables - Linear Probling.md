# Hash Tables - Linear Probing

### Motivation

In Hash Tables, when there is a collision, we must have a collision resolution technique when keys are hashed to the same bucket. Linear Probing is an example of a collision resolution technique. This technique is a part of open addressing.

### Example

Let's illustrate Linear Probing with an example. 

We now use a hash function as "key mod 7", and the keys to be insert are 50,700, 76, 85, 92, 73, 101.



<img src ="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2015/08/openAddressing1.png">



When we try to insert 85, (85 mod 7 = 1), we find that slot(1) is occupied by 50. So we insert 85 to the next free slot(2). 

One of the biggest issue of linear probing happens when insert 73. slot(6) is already occupied. You need to go from slot(6) to slot(3), which is time consuming.

















