# Simple Bank Management System

A simple command-line banking application written in Python. The program allows users to create bank accounts, log in, view account information, manage balances, and transfer money between accounts.

## Features

- Create a new bank account
- Generate an account number automatically
- Create and validate a 4-digit PIN
- Log in using an account number and PIN
- View account details
- Check account balance
- Deposit money
- Withdraw money
- Transfer money to another account
- Logout from an account
- Exit the application

## How It Works

The application stores account information in a Python dictionary named `accounts`.

Each account contains:

- **Name**
- **Mobile number**
- **4-digit PIN**
- **Balance**

New accounts start with a balance of `₹0`.

The application presents a main menu where the user can open an account, log in, or exit. After a successful login, an account menu provides banking operations such as deposits, withdrawals, and transfers. The implementation uses an in-memory dictionary, so account data is not persisted after the program terminates. fileciteturn0file0L5-L17

## Requirements

- Python 3.x
- No external libraries are required.

## Installation

1. Make sure Python 3 is installed.
2. Download or clone this project.
3. Open a terminal in the project directory.

## Running the Program

Run:

```bash
python main.py
```

## Main Menu

When the program starts, it displays:

```text
1. Open New Account
2. Login to Account
3. Exit
```

### 1. Open New Account

The user provides:

- Name
- Mobile number
- 4-digit PIN

The program validates that the PIN contains exactly four digits and then creates an account with an automatically generated account number and an initial balance of zero. fileciteturn0file0L19-L44

### 2. Login to Account

Users log in using their account number and PIN. A successful login opens the account management menu. fileciteturn0file0L47-L62

## Account Menu

After logging in, users can select:

```text
1. Account Details
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. Logout
```

The available operations are implemented in the account menu. fileciteturn0file0L64-L76

### Account Details

Displays:

- Account number
- Name
- Mobile number
- Current balance fileciteturn0file0L78-L89

### Check Balance

Displays the user's current account balance. fileciteturn0file0L91-L95

### Deposit Money

The user enters an amount to deposit. Only amounts greater than zero are accepted. fileciteturn0file0L97-L110

### Withdraw Money

The user enters an amount to withdraw. The program checks that:

- The amount is greater than zero.
- The requested amount does not exceed the available balance.

fileciteturn0file0L112-L131

### Transfer Money

Money can be transferred to another existing account. The program prevents:

- Transfers to non-existent accounts
- Transfers to the same account
- Transfers greater than the available balance
- Transfers of zero or negative amounts

fileciteturn0file0L133-L163

### Logout

Selecting `6` logs the user out and returns to the main menu. fileciteturn0file0L165-L178

## Data Storage

The project currently stores all account data in memory using a Python dictionary:

```python
accounts = {}
```

Because there is no database or file-based storage, all accounts and balances are lost when the program exits. fileciteturn0file0L5-L5

## Example Workflow

```text
WELCOME TO ABC BANK

1. Open New Account
2. Login to Account
3. Exit

> 1

----- OPEN NEW ACCOUNT -----

Enter your name: Gourav
Enter mobile number: 9876543210
Create 4 digit PIN: 1234

Account created successfully!
Your Account Number is: 1001
```

The user can then log in with the generated account number and PIN and perform banking operations.

## Project Structure

```text
.
├── main.py
└── README.md
```

## Limitations

This is a simple educational banking project. In its current form:

- Account data is stored only in memory.
- PINs are stored directly rather than securely hashed.
- There is no database.
- There is no transaction history.
- There is no persistent user authentication system.
- Input handling is basic.

## Possible Future Improvements

- Add SQLite or another database for persistent storage.
- Hash PINs instead of storing them directly.
- Add transaction history.
- Add account deletion and account updates.
- Improve input validation and error handling.
- Add transaction limits.
- Add an administrative interface.
- Separate the application into classes and modules.
- Add automated tests.

## License

This project does not currently specify a license.
