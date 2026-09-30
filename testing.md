# Testing

## Simple Bank Management System

Testing is based on the functionality implemented in the uploaded Python program.

| Test ID | Test Case | Input/Condition | Expected Result |
|---|---|---|---|
| TC-01 | Open account | Valid name, mobile and 4-digit PIN | Account is created and account number is displayed |
| TC-02 | Invalid PIN | PIN with fewer/more than 4 digits | Invalid PIN message is displayed |
| TC-03 | Non-numeric PIN | PIN containing letters | Invalid PIN message is displayed |
| TC-04 | Login success | Existing account and correct PIN | Login successful |
| TC-05 | Wrong PIN | Existing account and incorrect PIN | Wrong PIN message |
| TC-06 | Unknown account | Account number not in dictionary | Account not found message |
| TC-07 | Check balance | Logged-in account | Current balance is displayed |
| TC-08 | Valid deposit | Positive amount | Balance increases |
| TC-09 | Invalid deposit | Zero or negative amount | Invalid amount message |
| TC-10 | Valid withdrawal | Positive amount within balance | Balance decreases |
| TC-11 | Excess withdrawal | Amount greater than balance | Insufficient Balance message |
| TC-12 | Invalid withdrawal | Zero or negative amount | Invalid amount message |
| TC-13 | Valid transfer | Existing receiver and sufficient balance | Sender decreases and receiver increases |
| TC-14 | Unknown receiver | Receiver account does not exist | Receiver account not found |
| TC-15 | Self transfer | Receiver equals sender | Self-transfer is rejected |
| TC-16 | Transfer without funds | Amount greater than sender balance | Insufficient Balance message |
| TC-17 | Logout | Select logout | User returns to main menu |
| TC-18 | Exit | Select exit | Program terminates |

### Testing Approach
The project can be tested manually by executing each menu option and entering both valid and invalid inputs. The main focus is checking account creation, authentication, balance changes, and transaction validation.

### Limitation
The source code does not contain an automated test suite, so the above cases are proposed manual test cases derived from the implemented behavior.
