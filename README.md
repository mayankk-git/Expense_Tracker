# Python Learning Project: Expense Tracker

This repository is dedicated to learning and strengthening my knowledge of core Python concepts, specifically **Object-Oriented Programming (OOP)**, **file handling**, and **exception handling**. I am updating this repository daily to document my progress and learnings.

---

## 🚀 Daily Progress Log

### Day 1: Project Base & Core Logic
Built the initial foundational script, establishing the core mechanics and code execution flow.
* **Core Functions:** Implemented `add_expense()`, `show_expense()`, and `calculate_total()`.
* **Exception Handling:** Utilized `try` and `except` blocks to safely handle runtime errors and invalid user inputs, preventing application crashes.
* **Interactive CLI:** Built a user-interactive terminal menu using a `while` loop allowing continuous task selection.

### Day 2: Object-Oriented Refactoring
Restructured the procedural codebase into an Object-Oriented Programming (OOP) architecture for better structure and scalability.
* **Class Design:** Replaced standalone functions with dedicated classes and methods.
* **`Expense` Class:** Encapsulates individual expense data (storing `amount`, `category`, and `description`).
* **`ExpenseTracker` Class:** Handles tracker operations, offering methods to add expenses, display logged data, and compute total expenditure.
* **Verification:** Instantiated class objects, added test entries, validated the display formatting, and confirmed total calculations.

### DAY-3: JSON File Handling & CLI Integration

When working with Python, data stored in variables or class instances only exists in volatile memory (RAM)—meaning it disappears as soon as the program terminates. To make data persistent, it must be written to disk. JSON (JavaScript Object Notation) is one of the most popular lightweight formats for doing this.

Integrated persistent storage using JSON and streamlined user interaction through an expanded Command Line Interface (CLI).


1. **Implemented Data Persistence:** Integrated Python's built-in `json` module (`import json`) to store expense records persistently on disk.
2. **Added Storage Logic:** Created a new `save_expenses()` method utilizing `json.dump()` to serialize and save expense objects into a structured JSON file format.
3. **Enhanced Interactive CLI:** Updated the terminal menu system to seamlessly interact with all tracker features:
* `add_expense()` – Log new expenses
* `show_expenses()` – Display all recorded expenses
* `calculate_total()` – Sum up total spending
* `save_expenses()` – Save current data to the JSON file

---



## 🛠️ Concepts Practiced
- [x] Basic Python Control Flow & Functions
- [x] Exception & Error Handling (`try-except`)
- [x] Object-Oriented Programming (Classes, Objects, Methods
- [x] File handling with JSON module to store Python data (dump)
 
