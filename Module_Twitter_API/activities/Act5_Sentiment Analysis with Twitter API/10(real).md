<!--title="Regular Expressions [Quantifiers]"-->

## Regular Expressions [Quantifiers]

<img src="https://static.propublica.org/images/loops/loopfnct.gif" style="zoom:25%;" />

> With any set of rules specifying a language, you need rules that take care of strings or information that come in a variable size or length. You need loops or **Quantifiers** telling how big something(in this case a string is)!

Let's get into it:



* "*" specifies a string or character that repeats zero or more times in a bigger string.
  * For example, /hi*/ --> accepts --> h,hi, hiiii, hiiiiiiiiiiiiiiiiiiiiiiiiii, hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii and beyond

* "+" specifies a string or character that repeats one or more times in a bigger string.
  * For example, /hi*/ --> accepts --> hi, hiiii, hiiiiiiiiiiiiiiiiiiiiiiiiii, hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii, and beyond (notice h doesn't show up here).

* "?" specifies a string or character that repeats one or zero times in a bigger string.
  * For example, /hi?/ --> accepts --> hi or h.

* "{#}" specifies a string or character that repeats # times in a bigger string.
  * For example, /hi{3}/ --> accepts --> hiii.
* Adding a comma accepts strings with a character or string that is greater than equal to the specified length. So something like /hi{3,}/ accepts hiii,hiiiii, and above.
  * Adding a comma and number gives a range. For example, /hi{3,5}/ accepts hiii,hiiii,hiiiii.
  
* Finally adding a pair of parenthesis specifics a group of characters. Meaning you can now accept string with repeated *sequence* of characters.
  * For example, /he(llo)*/ --> accepts --> he,hello,hellollollollollollo and beyond.
* Similarly, you can use all the above mentioned specifiers on these sequences too!
  

***

Sources:

* https://regexr.com/
* https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285