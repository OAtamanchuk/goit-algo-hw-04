## Description
This repository contains solutions for Homework 4 of the GoIT Python course.
The project includes multiple independent tasks that demonstrate practical skills such as file processing, data parsing and building a basic console assistant bot.

## Technologies & Stack

The project is implemented using:
- Python 3
- Standard Python libraries:
  - sys - command-line arguments handling
  - pathlib - filesystem paths
  - datetime - date handling
- Third-party libraries:
  - colorama - colored console output
- Core programming concepts
  - Context managers (with)
  - Exception handling (try-except)
  - Functions and tuples
  - Dictionaries and lists
  - Recursive directory traversal

## Functionality

The repository includes implementations of the following tasks:

1. Salary File Analysis 

Reads a text file containing developer names and salaries.
Calculates total salary amount, average salary. Returns a tuple (total, average). 
Uses context managers for safe file handling. Handles missing or invalid files using exception handling.

2. Cats Information Parser 

Reads a text file with cat data (id,name,age).
Converts each line into a dictionary with keys:
- id
- name
- age

Returns a list of dictionaries.
Includes error handling and file parsing logic.

3. Directory Structure Visualizer 

CLI script that displays the structure of a directory.
Accepts a directory path as a command-line argument.
Recursively traverses directories and files.
Uses colorama to visually distinguish directories and files.
Handles invalid paths and input errors.

4. Console Assistant Bot (CLI)

Interactive command-line assistant bot.

Supports commands:
- hello
- add <name> <phone>
- change <name> <phone>
- phone <name>
- all
- exit / close

Designed as a prototype for a future assistant application.
