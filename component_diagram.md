# Component Diagram

## Simple Bank Management System

The system is implemented as a single Python program. Its main components are represented by the menu-driven interface, account management logic, account data store, authentication logic, and transaction operations.

```mermaid
flowchart TD
    U[User] --> M[Main Menu]
    M --> OA[Open New Account]
    M --> L[Login]
    M --> E[Exit]

    OA --> V[Validate 4-digit PIN]
    V --> D[(accounts dictionary)]
    D --> N[Generate Account Number]

    L --> A[Check Account Number]
    A --> P[Verify PIN]
    P --> AM[Account Menu]

    AM --> AD[Account Details]
    AM --> CB[Check Balance]
    AM --> DE[Deposit Money]
    AM --> WI[Withdraw Money]
    AM --> TR[Transfer Money]
    AM --> LO[Logout]

    AD --> D
    CB --> D
    DE --> D
    WI --> D
    TR --> D
