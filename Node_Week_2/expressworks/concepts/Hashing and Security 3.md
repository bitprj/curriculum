<!--title={A Closer Look at Hashing and Security}-->

in order to securely handle data, we must encrypt it so that no one can read the data without the key. 

An **SHA-1** (Secure Hash Algorithm 1) is a cryptographic hash function which takes an input and produces a hash value known as a message digest. This message is one way to securly store data.

 The SHA-1 can be computed like this in express:

```js
require('crypto') //The crypto module provides cryptographic functionality
  .createHash('sha1') //Creates and returns a Hash object that can be used to generate hash digests using the given algorithm
  .update(new Date().toDateString() + id) //Updates the hash content with the given data, in this case the current date and the message ID.
  .digest('hex') //Calculates the digest of all of the data passed to be hashed
//'hex' is how the digest is encoded

```

