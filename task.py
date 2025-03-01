class ATM:
    def __init__(self, account_balance=0, pin="1234"):
        """Initialize the ATM with an account balance and a PIN."""
        self.account_balance = account_balance
        self.pin = pin
        self.transaction_history = []

    def check_balance(self):
        """Return the current account balance."""
        return self.account_balance

    def withdraw(self, amount):
        """Withdraw cash from the account if sufficient balance exists."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrawal successful! New balance: ${self.account_balance}"
        else:
            return "Insufficient funds."

    def deposit(self, amount):
        """Deposit cash into the account."""
        self.account_balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        return f"Deposit successful! New balance: ${self.account_balance}"

    def change_pin(self, new_pin):
        """Change the account PIN."""
        self.pin = new_pin
        return "PIN changed successfully."

    def transaction_history(self):
        """Return the transaction history."""
        return self.transaction_history

def main():
    """Main function to simulate ATM operations."""
    atm = ATM()
    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            print(f"Your balance is: ${atm.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '4':
            new_pin = input("Enter new PIN: ")
            print(atm.change_pin(new_pin))
        elif choice == '5':
            print("Transaction History:")
            for transaction in atm.transaction_history:
                print(transaction)
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()