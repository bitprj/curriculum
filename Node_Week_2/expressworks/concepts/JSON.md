<!--title={JSON}--> 

JSON stands for **J**ava**S**cript **O**bject **N**otation and is a common data format for interchange between web servers. JSON is built upon two structures: 

* A collection of name/value pairs. In various languages, this is realized as an *object*, record, struct, dictionary, hash table, keyed list, or associative array.

  

  An *object* is an unordered set of name/value pairs. An object  begins with `{`left brace and ends  with `}`right brace. Each name is followed  by `:`colon and the name/value pairs are  separated by `,`comma. Here's a visual depiction:

  ![image](https://www.json.org/img/object.png)

  

* An ordered list of values. In most languages, this is realized as an *array*,    vector, list, or sequence.

  

  An *array* is an ordered collection of values. An array begins  with `[`left bracket and ends  with `]`right bracket. Values are separated  by `,`comma.

![image](https://www.json.org/img/array.png)





Here's an example of a JSON object that we call `superheroes`: 

```json
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```

You can access the `active` variable in using the `.` or brackets `[]`. Both would output `true`. 

```js
superHeroes.active
superHeroes['active']
```

You can also index lists. Accessing `superHeroes['members'][1]` outputs the following: 

```json
{
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
}
```



Here's some other useful tips: 

* JSON is purely a data format — it contains only properties, no methods.
* JSON requires double quotes to be used around strings and property names. Single quotes are not valid.
* Even a single misplaced comma or colon can cause a JSON file to go  wrong, and not work. You should be careful to validate any data you are  attempting to use (although computer-generated JSON is less likely to  include errors, as long as the generator program is working correctly).  You can validate JSON using an application like [JSONLint](http://jsonlint.com/).
* JSON can actually take the form of any data type that is valid for  inclusion inside JSON, not just arrays or objects. So for example, a  single string or number would be a valid JSON object.
* Unlike in JavaScript code in which object properties may be unquoted, in JSON only quoted strings may be used as properties.