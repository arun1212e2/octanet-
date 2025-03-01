import time

def display_menu():
    print("""
        1 == Check Balance
        2 == Withdraw Balance
        3 == Deposit Balance
        4 == Change PIN
        5 == Transaction History
        6 == Exit
    """)

def main():
    print("Please insert Your CARD")
    time.sleep(5)

    password = 2029
    balance = 100000
    transaction_history = []

    # Taking ATM pin from user
    try:
        pin = int(input("Enter your ATM pin: "))
    except ValueError:
        print("--Invalid input! Please enter a numeric PIN--")
        return

    # Checking if pin is valid
    if pin == password:
        while True:
            display_menu()
            try:
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("Please enter a valid option!!!")
                continue
            
            if option == 1:
                print(f"Your current balance is: {balance}")
            elif option == 2:
                try:
                    withdraw_amount = int(input("Please enter the amount to withdraw: "))
                    if withdraw_amount > balance:
                        print("Insufficient balance!")
                    else:
                        balance -= withdraw_amount
                        transaction_history.append(f"Withdrew: {withdraw_amount}")
                        print(f"{withdraw_amount} is debited from your account.")
                        print(f"Your updated balance is: {balance}")
                except ValueError:
                    print("Please enter a valid amount!")
            elif option == 3:
                try:
                    deposit_amount = int(input("Please enter the amount to deposit: "))
                    balance += deposit_amount
                    transaction_history.append(f"Deposited: {deposit_amount}")
                    print(f"{deposit_amount} is credited to your account.")
                    print(f"Your updated balance is: {balance}")
                except ValueError:
                    print("Please enter a valid amount!")
            elif option == 4:
                try:
                    new_pin = int(input("Enter your new PIN: "))
                    if new_pin == pin:
                        print("New PIN cannot be the same as the old PIN.")
                    else:
                        pin = new_pin
                        print("Your PIN has been changed successfully.")
                except ValueError:
                    print("Please enter a valid numeric PIN!")
            elif option == 5:
                print("Transaction History:")
                if transaction_history:
                    for transaction in transaction_history:
                        print(transaction)
                else:
                    print("No transactions have been made.")
            elif option == 6:
                confirm_exit = input("Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm_exit == 'yes':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    continue
            else:
                print("Invalid option! Please choose a valid option.")
    else:
        print("--Wrong PIN! Please try again--")

if _name_ == "_main_":
    main()