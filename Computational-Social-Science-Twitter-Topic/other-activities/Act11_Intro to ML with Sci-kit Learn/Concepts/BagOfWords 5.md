# Bag Of Words

We first train our Bag of Words with some sample text

Let's say we have the following string

```python
s1 = "The apple is red"
```

We store this phrase into our corpus (our known words).



Now we want to transform other strings into vectors based on the first sentence.

Let's say we want a vectorized version of:

```python
s2 = "The orange is not red"
```

Our corpus knows the words "The", "apple", "is", and "red".

The words in `s2` that are also in our corpus (currently only `s1`) are "The", "is", and "red". These words have a value of 1 in the final vector, while the other two words "orange" and "not" have a value of 0 because they are not in our corpus (`s1`).

```
Corpus: ["The", "apple", "is", "red"]
# s2 was "The orange is not red"
# after Bag of Words, it is [1, 0, 1, 0, 1]

[	1		  0		  1		 0		 1		]
	The		orange	 is		not		red
```

"The" 		  &rarr; inside corpus 	 		&rarr; 1

"orange" 	&rarr; not inside corpus	   &rarr; 0

"is"			   &rarr; inside corpus			 &rarr; 1

"not"			&rarr; inside corpus 			&rarr; 0

"red"			&rarr; not inside corpus  	&rarr; 1

So our final vector for "The orange is not red" is

```python
[1, 0, 1, 0, 1]
```

