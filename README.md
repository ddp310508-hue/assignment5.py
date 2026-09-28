# Lab Assignment 5: Introduction to String

**Course:** School of Computer Engineering and Technology  
**Assignment No:** 5  

## Problem Statement
Introduction to string

## Aim
Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

## Objectives
1. To learn the basics of string and it's operation.
2. To learn the Variable declaration, User input and output using string in python programming.

## Theory

### 1. Strings (Update, Slicing, Delete, Immutability)
* **String Definition:** A string is a sequence of characters enclosed in single, double, or triple quotes.
* **String Immutability:** Strings in Python are immutable, meaning once created, their elements cannot be changed or modified in place. 
* **Update:** Because of immutability, you cannot update a specific index directly (`str[0] = 'a'` throws an error). To update a string, you must construct a new string by joining parts of the old one.
* **Slicing:** Accessing substrings using the syntax `string[start:stop:step]`. Example: `"Python"[0:2]` returns `"Py"`.
* **Delete:** You cannot delete individual characters from a string. However, you can delete the entire string variable using the `del` keyword (`del my_string`).

### 2. Regular Expressions in Strings
Regular Expressions (Regex) provide a powerful tool for pattern matching and string manipulation via Python's built-in `re` module. 
* **Example:** The regex pattern `^[a-zA-Z0-9]+$` matches any string that contains only alphanumeric characters from start (`^`) to end (`$`) and has at least one character (`+`).

## Platform
Windows/Ubuntu - Python Editor (Jupyter Notebook, IDLE, or any IDE).

## Algorithm/Pseudo code
1. Start the program.
2. Import the regular expressions module (`re`).
3. Define a function or compilation pattern that checks if a string matches only `a-z`, `A-Z`, and `0-9`.
4. Accept a string input from the user.
5. Use `re.match()` or `re.search()` to evaluate the string against the alphanumeric pattern.
6. If the pattern matches the entire length of the input string, print a success message.
7. If it fails, print a message indicating invalid characters are present.
8. End the program.

## Input and Output
### Test Case 1: Valid Alphanumeric Input (Success)
**Input:**
```text
Enter a string to check: Python123
```
**Output:**
```text
Success: The string 'Python123' contains ONLY valid characters (a-z, A-Z, 0-9).
```

### Test Case 2: Invalid Input with Special Characters/Spaces (Failure)
**Input:**
```text
Enter a string to check: Hello @ World!
```
**Output:**
```text
Failure: The string 'Hello @ World!' contains unauthorized special characters or spaces.
```

## Conclusion
Studied strings basic operation with regular expression.

## FAQs

### 1. What is a string in Python? How do you create a string variable?
A string is an immutable sequence of Unicode characters. You create a string variable by assigning a text literal wrapped in quotes to a variable identifier.  
*Example:* `my_str = "Hello World"`

### 2. What are characters in a string? Give examples of valid characters from the English alphabet and digits.
Characters are the individual units or symbols that make up a string. 
* *Valid lowercase English letters:* `a, b, c, ..., z`
* *Valid uppercase English letters:* `A, B, C, ..., Z`
* *Valid digits:* `0, 1, 2, ..., 9`

### 3. What is the purpose of checking the characters in a string in a program?
Checking characters (input validation) ensures data integrity and security. It prevents injection attacks, crashes, and syntax runtime errors by verifying that user-provided text matches formatting requirements (e.g., verifying usernames, passwords, zip codes, or phone numbers) before processing it.

### 4. Which Python functions or methods can be used to check if a string contains only letters and numbers?
* **Built-in method:** The `.isalnum()` string method returns `True` if all characters in the string are alphanumeric.
* **Regex function:** The `re.match(pattern, string)` or `re.search(pattern, string)` functions from the `re` module can be used with the regex pattern `^[a-zA-Z0-9]+$`.
