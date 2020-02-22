<!--title="Regular Expressions [Anchors]"-->

## Regular Expressions [Anchors]

Lets start out with the basics:

* We start our Regular Expressions by opening up a "/" and writing all the rules between that and "/".
  * Something like: /RULES/ 

* "^" and "$" are called anchors and matches(or finds/extracts) a specified string or character within a larger string  at the start or just the end,respectively.
  * So when we write \^wow,\ the following string gets accepted : "wow, you are learning a lot!". 
  * When we write \\$bye!\ the following gets accepted: "nice work, bye!"
  * Now let's combine them: \\^Eat $vegetables\ --> accepts --> "Eat more vegetables".



***

Sources:

* https://regexr.com/
* https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285