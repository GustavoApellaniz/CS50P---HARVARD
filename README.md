# CS50P — Introduction to Programming with Python

Solutions, exercises, and final project from [Harvard University's CS50P](https://cs50.harvard.edu/python/), a course focused on Python programming, computational thinking, and problem-solving.

This repository documents my learning journey through CS50P, combining programming exercises and problem sets with a final project that applies the concepts learned throughout the course.

## About the Course

CS50P introduces the fundamentals of programming using Python. Throughout the course, I practiced writing functions, working with different data types, handling errors, processing files, using libraries, testing code, and designing programs with object-oriented principles.

The goal of this repository is to demonstrate my practical experience with Python, document my progress, and build a foundation for more advanced programming projects.

## Topics Covered

### Week 0 — Functions, Variables

- Defining and calling functions.
- Working with variables and data types.
- Receiving user input and displaying output.
- Using arithmetic and basic expressions.

### Week 1 — Conditionals

- Boolean expressions and comparison operators.
- `if`, `elif`, and `else` statements.
- Logical operators.
- Implementing decision-making logic.

### Week 2 — Loops

- `for` and `while` loops.
- Iteration and repetition.
- Using `range()` and sequences.
- Controlling program flow.

### Week 3 — Exceptions

- Handling runtime errors.
- Using `try` and `except`.
- Validating user input.
- Making programs more robust when unexpected input is provided.

### Week 4 — Libraries

- Importing and using Python modules.
- Exploring built-in functions and external libraries.
- Using existing functionality to solve problems more efficiently.

### Week 5 — Unit Tests

- Understanding software testing.
- Writing tests with `pytest`.
- Checking expected results and edge cases.
- Identifying and correcting bugs.

### Week 6 — File I/O

- Reading and writing files.
- Processing text and structured data.
- Working with file paths and file operations.
- Automating tasks involving stored information.

### Week 7 — Regular Expressions

- Understanding regular expressions.
- Pattern matching and text validation.
- Extracting and manipulating text.
- Using Python's `re` module.

### Week 8 — Object-Oriented Programming

- Creating classes and objects.
- Defining constructors with `__init__`.
- Working with instance attributes and methods.
- Using getters and setters.
- Representing objects with `__str__`.
- Modeling relationships between objects.

### Week 9 — Et Cetera

- Exploring additional Python concepts.
- Strengthening programming fundamentals.
- Applying previously learned concepts to more complex problems.

*The topics above summarize the course curriculum; the repository folders contain the exercises and implementations available in this project.*

## Repository Structure

Each folder corresponds to a week or problem set from CS50P.

```text
CS50P---HARVARD/
├── Week 0/
├── Week 1/
├── Week 2/
├── Week 3/
├── Week 4/
├── Week 5/
├── Week 6/
├── Week 7/
├── Week 8/
├── Week 9/
└── Final Project/
```

*The structure above is illustrative. Folder names may differ depending on the actual repository organization.*

## Final Project — Car Dealership Management System

As a practical application of the concepts studied throughout CS50P, I developed a **Car Dealership Management System** using Python and Object-Oriented Programming.

The project models manufacturers, vehicle models, and individual cars through three interconnected classes.

### Main Classes

- **`Montadora`** — Represents a vehicle manufacturer, storing its code, state, and company name.
- **`Modelo`** — Represents a vehicle model and maintains a reference to its manufacturer.
- **`Carro`** — Represents a vehicle, storing its license plate, model, and manufacturing year.

### Main Features

The application uses a command-line menu to organize the intended operations:

- Register manufacturers.
- Register vehicle models associated with manufacturers.
- Register cars associated with vehicle models.
- List registered manufacturers.
- List registered models.
- List registered cars.
- Exit the application.

### Concepts Applied

The project brings together several Python concepts:

- Class design and object instantiation.
- Constructors, attributes, and instance methods.
- Getters and setters.
- Relationships and references between objects.
- Lists for storing collections of objects.
- String representations with `__str__`.
- User input and basic exception handling.
- Menu-driven application logic.

The project currently uses in-memory lists, making it a practical exercise in modeling data and managing relationships between objects. Further improvements include input validation, correcting registration workflows, and adding persistent storage.

## Skills Developed

Through the course exercises and final project, I practiced:

- **Python fundamentals:** variables, functions, data types, conditionals, and loops.
- **Problem-solving:** breaking programming problems into smaller, manageable steps.
- **Error handling:** anticipating invalid input and handling exceptions.
- **Testing:** checking program behavior and identifying bugs.
- **File processing:** reading and writing data.
- **Text processing:** using libraries and regular expressions.
- **Object-oriented design:** organizing code into classes and modeling real-world entities.
- **Independent development:** applying course concepts to build a project beyond isolated exercises.

## Learning Goals

This repository represents my ongoing development as a Python programmer. My focus is on strengthening programming fundamentals, writing clearer and more maintainable code, improving debugging skills, and applying what I learn to practical projects.

## Acknowledgments

Thanks to Harvard University and the CS50 team for providing the CS50P course and learning materials.

- [Official CS50P Course](https://cs50.harvard.edu/python/)
- [CS50P Problem Sets](https://cs50.harvard.edu/python/psets/)

## Author

**Gustavo Fraga Apellaniz**

GitHub: [@GustavoApellaniz](https://github.com/GustavoApellaniz)

---

*This repository is a record of my practical learning and progress through Harvard's CS50P — Introduction to Programming with Python.*
