# name 

Creating the `Graph` Class Autograder

# cards_folder 

Module4_Labs/Lab3_File_System/Cards/

# checkpoint_type 

Autograder 

# instruction 

Submit the all code you have completed thus far, including your `Graph` class. By now, your code should be able to read in the input files and the `Graph` class should be able to handle:

* Storing and adding edges
* Storing values (folder/file names) of each node in the graph

At the end of your main function, add the following lines of code (needed for testing). Please note that you may need to adjust variable names depending on what you chose to name `edges` and `val_map`. This code prints out all the edges tuples and the contents of the `val_map` in a **sorted** manner:

```python
	print("Edges:")
	for edge in sorted(edges):
		print(edge)
	print("Values:")	
	for number in sorted(val_map):
		print(number, val_map[number])	
```

Submission can be done from Command-Line Interface (CLI) or through a `src.zip` file that you can drag and drop.

# test_file_location

Module4_Labs/Lab3_File_System/Student-Starter/Checkpoints/2-Checkpoint-Tests/