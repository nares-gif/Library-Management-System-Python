# Library-Management-System-Python
Python Library Management System designed with the Repository pattern to isolate business logic from data storage.
## Library Management System

A simple CLI-based library management system built with Python. Supports adding, issuing, returning, searching, and deleting books, with data persisted to a local JSON file.

Built with a layered architecture (Repository pattern) to separate data access (`BookRepository`) from business logic (`LibraryService`), keeping the codebase testable and maintainable.

**Features:**
- Add, search, and delete books
- Issue and return books with borrower tracking
- Persistent storage using JSON
- Clean separation of concerns (Repository + Service layers)

**Tech stack:** Python (standard library only — `json`, `datetime`)
