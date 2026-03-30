# Python CLI Contact Manager

A command-line contact manager built while learning Python and backend programming fundamentals.

This project is part of my daily Python practice and focuses on building real programs rather than isolated exercises. The application runs entirely in the terminal and allows users to manage contacts through a simple CLI interface.

---

## Purpose

The goal of this project is to practice core programming and backend concepts such as:

- working with dictionaries and nested dictionaries
- designing command-line applications
- managing program state
- implementing CRUD operations
- organizing Python code across modules

The project is built incrementally with daily improvements.

---

## Features

The contact manager allows users to:

- Add contacts
- Search for contacts
- Update contact information
- Delete contacts
- Display all stored contacts
- Exit the program safely

---

## Example Data Structure

Contacts are stored using a nested dictionary structure.

Example:


contacts = {
"Andrew": {
"email": "andrew@email.com
",
"phone": "08012345678"
},
"John": {
"email": "john@email.com
",
"phone": "09012345678"
}
}


Each contact name acts as the key, and the value stores the contact's information.

---

## Example CLI Menu


Welcome to Contact Manager

Add contact
Search contact
Update contact
Delete contact
Show contacts
Exit

---

## Project Structure


contact_manager/
│
├── main.py
├── storage.py


**main.py**

Handles the CLI interface, user input, and overall program flow.

**storage.py**

Stores the contacts dictionary used by the application.

---

## Learning Focus

This project reinforces important programming concepts including:

- dictionary data structures
- nested dictionaries
- CLI program architecture
- modular programming
- input handling
- data storage and retrieval

---

## Development Progress

The project is developed step-by-step over multiple days:

- Day 1 — Contact storage using dictionaries
- Day 2 — Display contacts
- Day 3 — Search contacts
- Day 4 — Delete contacts
- Day 5 — Update contacts
- Day 6 — Error handling and validation
- Day 7 — Refactoring and testing

---

## Status

Work in progress. The project is continuously improved as part of daily Python learning and practice.

---
