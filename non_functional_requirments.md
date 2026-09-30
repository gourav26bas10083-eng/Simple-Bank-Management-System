# Non-Functional Requirements

## Simple Bank Management System

### NFR-01: Usability
The system should be simple to operate through clear numbered menus and text prompts.

### NFR-02: Responsiveness
For the small in-memory data set used by this project, account lookup and balance operations should complete immediately during normal execution.

### NFR-03: Reliability
The system should validate basic inputs such as PIN length, positive transaction amounts, account existence, and sufficient balance.

### NFR-04: Maintainability
The code should remain readable through meaningful variable names, clear menu sections, and straightforward control flow.

### NFR-05: Portability
The program should be executable in a standard Python environment without requiring a database or additional external package.

### NFR-06: Data Availability
Account data is available only during the current execution of the program because the implementation uses in-memory storage.

### NFR-07: Security
The system provides basic PIN-based login. However, the current project does not implement advanced security measures such as encryption, hashing, or secure persistent storage.

### NFR-08: Performance
The simple dictionary-based storage is suitable for the small-scale educational project for which the program is designed.
