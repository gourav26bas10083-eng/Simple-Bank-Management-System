# Workflow

## Simple Bank Management System

```mermaid
flowchart TD
    A([Start]) --> B[Display Main Menu]
    B --> C{Choose Option}

    C -->|1| D[Enter Name, Mobile and PIN]
    D --> E{PIN is 4 digits?}
    E -->|No| D
    E -->|Yes| F[Create Account]
    F --> B

    C -->|2| G[Enter Account Number and PIN]
    G --> H{Account Exists?}
    H -->|No| B
    H -->|Yes| I{PIN Correct?}
    I -->|No| B
    I -->|Yes| J[Display Account Menu]

    J --> K{Choose Account Operation}
    K -->|Details| L[Display Account Details]
    K -->|Balance| M[Display Balance]
    K -->|Deposit| N[Validate Amount and Add]
    K -->|Withdraw| O[Validate Amount and Balance]
    K -->|Transfer| P[Validate Receiver and Balance]
    K -->|Logout| B

    L --> J
    M --> J
    N --> J
    O --> J
    P --> J

    C -->|3| Q([End])
    C -->|Invalid| B
```

### Overall Workflow
The program starts by displaying the main menu. The user can create an account, log in, or exit. After successful login, the account menu remains active until the user chooses logout. Banking operations update the account data stored in the `accounts` dictionary. The program returns to the main menu after logout and ends when the user chooses Exit.
