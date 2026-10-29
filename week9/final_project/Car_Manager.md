# Car Dealership Management System

A simple Python project that demonstrates **Object-Oriented Programming (OOP)** through a car dealership management system.

The application models car manufacturers, vehicle models, and individual cars. It uses classes, objects, methods, lists, and object relationships to organize and manage this information.

## Project Overview

The system is designed to manage three main entities:

- **Manufacturer (`Montadora`):** Stores the manufacturer's code, state, and company name.
- **Vehicle Model (`Modelo`):** Stores the model code, model name, and its associated manufacturer.
- **Car (`Carro`):** Stores the license plate, vehicle model, and manufacturing year.

Each entity is represented by a Python class with an initializer, getter methods, setter methods, and a string representation.

## Features

The application provides a menu-driven interface with the following operations:

| Option | Description |
|---|---|
| 1 | Register a manufacturer |
| 2 | Register a vehicle model |
| 3 | Register a car |
| 4 | List registered manufacturers |
| 5 | List registered vehicle models |
| 6 | List registered cars |
| 7 | Exit the application |

The registration workflow is intended to associate each vehicle model with an existing manufacturer and each car with an existing vehicle model.

## Object-Oriented Design

### 1. Manufacturer — `Montadora`

Represents a vehicle manufacturer.

**Attributes:**
- `cod_montadora`: Manufacturer code.
- `estado`: State associated with the manufacturer.
- `razao_social`: Company name.

**Methods:**
- Getters to retrieve attribute values.
- Setters to update attribute values.
- `__str__()` to provide a readable representation of the object.

### 2. Vehicle Model — `Modelo`

Represents a vehicle model produced by a manufacturer.

**Attributes:**
- `cod_modelo`: Model code.
- `nome_modelo`: Vehicle model name.
- `montadora`: Reference to a `Montadora` object.

The model stores a reference to the manufacturer object rather than simply storing its name. This demonstrates how Python objects can be connected to represent real-world relationships.

### 3. Car — `Carro`

Represents an individual vehicle.

**Attributes:**
- `atributos_placa`: License plate.
- `nome_modelo`: Reference intended to hold a `Modelo` object.
- `ano_fabricacao`: Manufacturing year.

The intended relationship allows each car to be associated with a specific model, which is itself associated with a manufacturer.

## Relationships Between Classes

```text
Montadora
   |
   | has a reference to
   v
Modelo
   |
   | has a reference to
   v
Carro
```

This structure illustrates object composition and references between objects.

For example, a vehicle model can access its manufacturer's information through the `montadora` attribute. A car can access its model through its model reference.

## Technologies Used

- **Python 3**
- Object-Oriented Programming
- Classes and objects
- Constructors (`__init__`)
- Instance attributes and methods
- Getters and setters
- Lists for in-memory data storage
- `try/except` for handling invalid menu input
- `__str__()` for object representation

## Getting Started

### Prerequisites

Install Python 3 on your computer.

### Run the project

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project-directory>
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

   Replace `main.py` with the actual filename if necessary.

4. Follow the menu instructions in the terminal.

No external Python packages are required by the code shown.

## Current Limitations

This project is an educational exercise and currently stores data in memory. Registered information is not saved after the program closes.

Some registration and listing functions still require corrections to ensure that object relationships, data types, and validation work consistently.

Potential improvements include:

- Correcting model and car registration workflows.
- Validating manufacturer and model codes.
- Converting numeric input to the appropriate data types.
- Improving error handling and menu navigation.
- Adding persistent storage using files or a database.
- Separating the classes and application logic into modules.
- Adding automated tests.

## Learning Objectives

The project provides practical experience with:

- Designing classes to represent real-world entities.
- Creating and managing object instances.
- Establishing relationships between objects.
- Using lists to store collections of objects.
- Implementing basic CRUD-style operations.
- Organizing a simple command-line application.
- Handling invalid user input.

## Author

**Gustavo Fraga Apellaniz**

GitHub: [@GustavoApellaniz](https://github.com/GustavoApellaniz)

---

*An educational Python project focused on Object-Oriented Programming and basic data management.*
