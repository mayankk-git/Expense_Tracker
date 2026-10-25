# Python Learning Project: Expense Tracker

This repository is dedicated to learning and strengthening my knowledge of core Python concepts, specifically **Object-Oriented Programming (OOP)**, **file handling**, and **exception handling**. I am updating this repository daily to document my progress and learnings.

---

## 🚀 Daily Progress Log

### Day 1: Project Base & Core Logic
Built the initial foundational script, establishing the core mechanics and code execution flow.
1. **Core Functions:** Implemented `add_expense()`, `show_expense()`, and `calculate_total()`.
2. **Exception Handling:** Utilized `try` and `except` blocks to safely handle runtime errors and invalid user inputs, preventing application crashes.
3. **Interactive CLI:** Built a user-interactive terminal menu using a `while` loop allowing continuous task selection.

### Day 2: Object-Oriented Refactoring
Restructured the procedural codebase into an Object-Oriented Programming (OOP) architecture for better structure and scalability.
1. **Class Design:** Replaced standalone functions with dedicated classes and methods.
2. **`Expense` Class:** Encapsulates individual expense data (storing `amount`, `category`, and `description`).
3. **`ExpenseTracker` Class:** Handles tracker operations, offering methods to add expenses, display logged data, and compute total expenditure.
4. **Verification:** Instantiated class objects, added test entries, validated the display formatting, and confirmed total calculations.

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


### DAY-4: JSON File Handling, Data Persistence & Feature Expansion
Implemented full read/write persistence using JSON and expanded the tracker's functionality with category filtering, item deletion, and indexed viewing.

1. **Automatic Data Saving:** Integrated `save_expenses()` directly into `add_expense()` so new entries are automatically written to disk without requiring explicit manual saving.
2. **Persistent Data Loading:** Implemented `load_expenses()` to deserialize JSON data back into Python lists upon startup. This prevents `save_expenses()` from overwriting pre-existing data on new entries.
3. **Robust Error Handling:** Wrapped file operations in `try` and `except` blocks to handle missing files (`FileNotFoundError`), corrupted files, and JSON decoding errors gracefully.
4. **Category Filtering:** Added `filter_category()` to isolate expenses by specific categories and calculate the cumulative total spent within that category.
5. **Item Deletion:** Added `delete_expense()` to allow users to remove specific entries from memory and sync the update back to the JSON file.
6. **Indexed Output:** Upgraded `show_expenses()` to output enumerated indices alongside entries, enabling accurate selection for deletion and filtering.


### Day 5: Input Validation Helpers, Index-Based Editing & Spending Analytics

Enhanced input robustness, enabled modifications of existing logs, and added automated spending analytics.
1. **Numeric Input Validation:** Created input helper functions to validate numeric inputs, ensuring expense amounts are positive values greater than zero and handling invalid inputs gracefully.
2. **String Input Validation:** Implemented category and description helpers to ensure user inputs are valid non-empty strings and not just empty spaces/whitespaces.
3. **Expense Editing (`edit_expense()`):** Added an `edit_expense()` method to the `ExpenseTracker` class allowing users to update specific expenses directly at the index level.
4. **Category Spending Summary:** Built a summary analysis method to calculate total expenditure breakdown per category and highlight the highest spending category automatically.

---



## 🛠️ Concepts Practiced
- [x] Basic Python Control Flow & Functions
- [x] Exception & Error Handling (`try-except`)
- [x] Object-Oriented Programming (Classes, Objects, Methods)
- [x] File handling with JSON module to store Python data (dump)
- [x] File handling with JSON module to retrieve json data (load)
- [x] Input validation and code reusability
 
