# Task 2

## 1. What are data structures?

Data structures are ways to store and organize data so we can use and update it easily.

| Data structure | Example use |
|---|---|
| List | Keeping a shopping cart or a list of students |
| Tuple | Storing fixed coordinates of a location |
| Set | Keeping unique email addresses |
| Dictionary | Storing student details using roll numbers as keys |
| Stack | Undo operation in a text editor |
| Queue | Print jobs waiting for a printer |
| Tree | File and folder structure |
| Graph | Routes between cities |

## 2. Reading task

Read Chapters 1 to 5 from the shared Learning Python book. This part is a reading activity; no written answer was requested. The book was not provided with these questions.

## 3. List of friends and list methods

See `03_list_methods.py`. The names are examples and can be changed. The program uses `dir()` and `help()` to explore the methods.

| Method | Use |
|---|---|
| append() | Add one item at the end |
| extend() | Add items from another iterable |
| insert() | Add an item at an index |
| remove() | Remove the first matching item |
| pop() | Remove and return an item |
| clear() | Remove all items |
| index() | Find the first index of an item |
| count() | Count how many times an item appears |
| sort() | Sort the list |
| reverse() | Reverse the list |
| copy() | Make a shallow copy |

## 4. Ordered and unordered data types

Ordered data types keep their elements in a particular order. Lists, tuples and strings are ordered and can be accessed by index. Dictionaries also preserve insertion order in Python 3.7 and later, but their values are accessed using keys.

Unordered data types do not guarantee a particular order. A set is an example. We cannot access a set by index.

## 5. Types of given values

| Value | Python type |
|---|---|
| `100` | int |
| `105.5` | float |
| `192.56j` | complex |
| `10+6j` | complex |
| `'10'` | str |
| `'hello world'` | str |
| `[10, 20, 50, 100]` | list |
| `{'name': 'sachin', 'age': 24, 'language': 'python'}` | dict |

The `05_value_types.py` program checks these using `type()`.
