# Design Decisions

## Simple Bank Management System

### 1. Dictionary for account storage
A Python dictionary named `accounts` is used to store account records. The account number acts as the key, while customer details, PIN, and balance are stored in a nested dictionary.

### 2. Menu-driven interface
The program uses numbered menus so that users can open an account, log in, perform banking operations, or exit the program.

### 3. PIN validation
A PIN is accepted only when it contains exactly four digits. This provides a simple validation rule for account creation.

### 4. In-memory storage
The current implementation stores all account information in memory. No database or external file is used, so the data exists only while the program is running.

### 5. Separate account menu
After successful login, the user enters a separate account menu. This keeps account operations grouped together and allows repeated transactions until logout.

### 6. Basic transaction validation
Deposit and withdrawal amounts must be positive. Withdrawal and transfer operations also check whether the available balance is sufficient.

### 7. Simple account numbering
The account number is generated using the current number of accounts, starting from 1001. This keeps account creation simple for the project.

These decisions match the implementation present in the uploaded Python source code. 
