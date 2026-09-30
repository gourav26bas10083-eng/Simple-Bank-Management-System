# Implementation Details

## Simple Bank Management System

### Programming Language
The project is implemented in Python.

### Data Structure
The program uses a dictionary:

```python
accounts = {}
```

Each account is stored using its account number as the key. The value contains:

- `name`
- `mobile`
- `pin`
- `balance`

### Main Program Loop
The application runs inside a `while True` loop. The main menu provides three choices:

1. Open New Account
2. Login to Account
3. Exit

### Account Creation
The user enters personal information and a PIN. The PIN is checked with:

```python
if len(pin) != 4 or not pin.isdigit():
```

A new account number is then generated from the number of accounts currently stored.

### Authentication
For login, the program first checks whether the account number exists. It then compares the entered PIN with the stored PIN.

### Account Operations
After successful authentication, another loop displays the account menu. The implemented operations are account details, balance checking, deposit, withdrawal, transfer, and logout.

### Deposit
A positive deposit amount is added directly to the current balance.

### Withdrawal
The program checks the amount and available balance before subtracting the amount.

### Transfer
The program verifies that the receiver exists, is not the current account, and that the sender has enough money. It then subtracts the amount from the sender and adds it to the receiver.

### Storage Limitation
The project does not use a database or file. Therefore, accounts are lost when the Python program stops.
