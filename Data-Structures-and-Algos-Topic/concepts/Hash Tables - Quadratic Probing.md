# concept_name
Quadratic Probing

# image_folder
curriculum/Module4.1_Intro_to_Data_Structures_and_Algos/activities/Act2_HashTables/Quadratic_Probing_Diagram.jpeg

# Quadratic Probing Step 1

## name
Reason to use Quadratic Probing

## md_content
```
# Motivation

In Hash Tables, when there is a collision, we must have a collision resolution technique when keys are hashed to the same bucket. Quadratic Probing is an example of a collision resolution technique. This technique is a part of open addressing.
```

# Quadratic Probing Step 2

## name
Conceptual Steps to implement Quadratic Probing

## md_content
```
# Preliminary Information<sup>1</sup> 

* We define our hash function to be h(k) = (k+j<sup>2</sup>) % (size of table)
* We define j as a counter variable which is initialized to 0 when attempting to insert an element into the hash table. If, when using the hash function, we have a collision, we increment j and recalculate where to insert the element using the new hash function.
```

# Quadratic Probing Step 3

## name
Example of implementing Quadratic Probing

## md_content
```
# Example<sup>2</sup>

Quadratic probing is best demonstrated through an example.

Say that we have a hash table of size 5. Let's try to insert the numbers 2, 7, and 22.

Notice how everytime there is a collision, we increment j and reapply the hash function h(k) = (k+j<sup>2</sup>) % (size of table).

```
## image
<img src ="https://projectbit.s3-us-west-1.amazonaws.com/darlene/labs/Quadratic_Probing_Diagram+.jpeg">

 











