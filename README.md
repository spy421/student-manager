# Student Manager

A simple student management application built with Python. The project allows users to manage student records through a command-line menu.

## Features

- View all students
- Add a new student
- Search for a student by name
- Delete a student
- Edit existing student information
- Validate user input
- Save student records to a JSON file
- Preserve data between program runs

## Technologies

- Python 3
- JSON
- Git and GitHub

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/spy421/student-manager.git
cd student-manager
```

### 2. Prepare the data file

Create a `students.json` file in the project directory with the following sample data:

```json
[
    {
        "name": "Dana",
        "age": 20,
        "major": "Computer Science"
    },
    {
        "name": "Alex",
        "age": 22,
        "major": "Data Analytics"
    }
]
```

### 3. Run the application

```bash
python3 main.py
```

## Project Structure

```text
student-manager/
├── main.py
├── students.json
├── .gitignore
└── README.md
```

Note: `students.json` is excluded from version control to avoid publishing personal data. Create the file locally before running the application.

## What I Learned

- Working with Python functions, loops, and conditional statements
- Managing lists and dictionaries
- Reading and writing JSON files
- Handling invalid user input with `try` and `except`
- Using Git and GitHub for version control
