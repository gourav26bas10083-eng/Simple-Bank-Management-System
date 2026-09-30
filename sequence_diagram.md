# Sequence Diagram

## Login and Transaction Flow

The following sequence describes a typical interaction in which a user logs in and deposits money.

```mermaid
sequenceDiagram
    actor User
    participant System as Bank System
    participant Accounts as accounts Dictionary

    User->>System: Select Login
    User->>System: Enter account number and PIN
    System->>Accounts: Check account number
    Accounts-->>System: Account found
    System->>Accounts: Compare stored PIN
    Accounts-->>System: PIN matches
    System-->>User: Login successful

    User->>System: Select Deposit
    User->>System: Enter amount
    System->>Accounts: Read current balance
    Accounts-->>System: Current balance
    System->>Accounts: Add deposit amount
    Accounts-->>System: Updated balance
    System-->>User: Deposit successful
