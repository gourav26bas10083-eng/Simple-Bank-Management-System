# ******************************************
#        SIMPLE BANK MANAGEMENT SYSTEM
# ******************************************

accounts = {}

while True:

    print("\n================================")
    print("       WELCOME TO ABC BANK")
    print("================================")
    print("1. Open New Account")
    print("2. Login to Account")
    print("3. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    # --------------------------------
    # OPEN NEW ACCOUNT
    # --------------------------------
    if choice == "1":

        print("\n----- OPEN NEW ACCOUNT -----")

        name = input("Enter your name: ")
        mobile = input("Enter mobile number: ")
        pin = input("Create 4 digit PIN: ")

        if len(pin) != 4 or not pin.isdigit():
            print("Please enter a valid 4 digit PIN.")
            continue

        account_number = str(1000 + len(accounts) + 1)

        accounts[account_number] = {
            "name": name,
            "mobile": mobile,
            "pin": pin,
            "balance": 0
        }

        print("\nAccount created successfully!")
        print("Your Account Number is:", account_number)
        print("Gourav")

    # --------------------------------
    # LOGIN
    # --------------------------------
    elif choice == "2":

        print("\n----- ACCOUNT LOGIN -----")

        account_number = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        if account_number in accounts:

            if accounts[account_number]["pin"] == pin:

                print("\nLogin Successful!")
                print("Welcome", accounts[account_number]["name"])

                # ACCOUNT MENU
                while True:

                    print("\n========== ACCOUNT MENU ==========")
                    print("1. Account Details")
                    print("2. Check Balance")
                    print("3. Deposit Money")
                    print("4. Withdraw Money")
                    print("5. Transfer Money")
                    print("6. Logout")
                    print("==================================")

                    option = input("Enter your choice: ")

                    # ACCOUNT DETAILS
                    if option == "1":

                        print("\n----- ACCOUNT DETAILS -----")
                        print("Account Number:",
                              account_number)
                        print("Name:",
                              accounts[account_number]["name"])
                        print("Mobile:",
                              accounts[account_number]["mobile"])
                        print("Balance: ₹",
                              accounts[account_number]["balance"])

                    # CHECK BALANCE
                    elif option == "2":

                        print("\nYour Balance is ₹",
                              accounts[account_number]["balance"])

                    # DEPOSIT
                    elif option == "3":

                        amount = float(input(
                            "Enter amount to deposit: ₹"))

                        if amount > 0:
                            accounts[account_number]["balance"] += amount

                            print("Money deposited successfully!")
                            print("New Balance: ₹",
                                  accounts[account_number]["balance"])
                        else:
                            print("Invalid amount.")

                    # WITHDRAW
                    elif option == "4":

                        amount = float(input(
                            "Enter amount to withdraw: ₹"))

                        balance = accounts[account_number]["balance"]

                        if amount <= 0:
                            print("Invalid amount.")

                        elif amount > balance:
                            print("Insufficient Balance!")

                        else:
                            accounts[account_number]["balance"] -= amount

                            print("Please collect your cash.")
                            print("Remaining Balance: ₹",
                                  accounts[account_number]["balance"])

                    # TRANSFER
                    elif option == "5":

                        receiver = input(
                            "Enter receiver Account Number: ")

                        if receiver not in accounts:
                            print("Receiver account not found.")

                        elif receiver == account_number:
                            print("You cannot transfer money to yourself.")

                        else:

                            amount = float(input(
                                "Enter transfer amount: ₹"))

                            balance = accounts[account_number]["balance"]

                            if amount <= 0:
                                print("Invalid amount.")

                            elif amount > balance:
                                print("Insufficient Balance!")

                            else:
                                accounts[account_number]["balance"] -= amount
                                accounts[receiver]["balance"] += amount

                                print("Money transferred successfully!")
                                print("Transferred ₹", amount)

                    # LOGOUT
                    elif option == "6":

                        print("You have been logged out.")
                        break

                    else:
                        print("Invalid choice!")

            else:
                print("Wrong PIN!")

        else:
            print("Account not found!")

    # --------------------------------
    # EXIT
    # --------------------------------
    elif choice == "3":

        print("\nThank you for using ABC Bank!")
        break

    else:
        print("Invalid choice!")

