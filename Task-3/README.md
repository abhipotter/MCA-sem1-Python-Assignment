# Task 3

## 1. Shallow copy and deep copy

A shallow copy creates a new outer object, but nested objects are still shared with the original. If we change a nested list, the change can be seen in both copies.

A deep copy also copies nested objects, so changes to the original nested list do not affect the copied list in this example.

See `01_shallow_deep_copy.py` for an example using `copy.copy()` and `copy.deepcopy()`.

## 2. Library management using lists

We can use a list of lists to keep records of books, students and issued books. Each inner list represents one record.

- Books: book ID, title, author and available quantity.
- Students: student ID, name and course.
- Issued books: book ID, student ID and issue date.

See `02_library_lists.py` for example records. All records are sample data.

## 3. Expression and statement

An expression is something that evaluates to a value, like `5 + 3` or `len('hello')`.

A statement is an instruction that Python executes, like `spam = 10` or an `if` statement. An assignment statement assigns a value to a variable. A statement can contain expressions.

## 4. Data types

### Atomic or primary data types

These represent basic individual values. Examples in Python are int, float, complex and bool. A string is also a basic built-in type, but it is a sequence of characters rather than an atomic type in the strict sense.

### Secondary and user-defined data types

Secondary or compound data types group multiple values. Examples are list, tuple, set and dictionary. A user-defined data type is a type created by the programmer using a class, such as a Student or Book class. Built-in compound types and user-defined types are not exactly the same thing in Python.

## 5. What is UDF?

UDF stands for User Defined Function. It is a function written by the programmer to perform a particular task. In Python we can define it using the `def` keyword.

```python
def add(a,b):
    return a+b

print(add(10,20))
```

Output: `30`
