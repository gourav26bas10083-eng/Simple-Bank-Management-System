# Functional Requirements

## Simple Bank Management System

### FR-01: Open New Account
The system shall allow a user to create a new bank account by entering a name, mobile number, and four-digit PIN.

### FR-02: Validate PIN
The system shall reject a PIN if it does not contain exactly four digits.

### FR-03: Generate Account Number
The system shall generate an account number for a newly created account and display it to the user.

### FR-04: Login
The system shall allow a user to log in using an account number and PIN.

### FR-05: Validate Login
The system shall display an error when the account number does not exist or when the entered PIN is incorrect.

### FR-06: View Account Details
After login, the user shall be able to view account number, name, mobile number, and current balance.

### FR-07: Check Balance
The user shall be able to check the current account balance.

### FR-08: Deposit Money
The system shall allow the user to deposit a positive amount and update the balance.

### FR-09: Withdraw Money
The system shall allow the user to withdraw money only when the amount is positive and does not exceed the available balance.

### FR-10: Transfer Money
The system shall allow the user to transfer a positive amount to another existing account, provided sufficient balance is available.

### FR-11: Prevent Self Transfer
The system shall reject a transfer when the receiver account is the same as the logged-in account.

### FR-12: Logout
The system shall allow the logged-in user to leave the account menu and return to the main menu.

### FR-13: Exit
The system shall allow the user to exit the application from the main menu.

### FR-14: Invalid Choices
The system shall display an appropriate message when an invalid menu choice is entered.
