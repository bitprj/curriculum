<!--title={Updating dictionary}-->

Dictionary are mutable. We can add new items or change the value of existing items using assignment operator.

You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown below in the simple example −

```python
# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
```

> Note: a dictionary allows you to dynamically add new keys with corresponding values or redefine values to an existing key following initialization.

The code snippet above should reflect the appropriate changes on _dict_ such that it contains a new key _'School'_ and that _'Age'_ no longer has value _'7'_.