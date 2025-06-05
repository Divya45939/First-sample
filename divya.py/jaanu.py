class ATM:
    def __init__(self, initial_balance=0, pin='1234'):
        """
        Initializes the ATM with an initial balance and a PIN.
        :param initial_balance: The initial balance of the account
        :param pin: The PIN for accessing the ATM
        """
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def display_balance(self):
        """Displays the current account balance."""
        print(f"Current balance: ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        :param amount: The amount to deposit
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"Successfully deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.
        :param amount: The amount to withdraw
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"Successfully withdrew: ${amount:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def change_pin(self, old_pin, new_pin):
        """
        Changes the account PIN.
        :param old_pin: The current PIN
        :param new_pin: The new PIN to set
        """
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect current PIN.")

    def view_transaction_history(self):
        """Displays the transaction history."""
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions have been made.")

def main():
    # Create an ATM instance with an initial balance of $1000 and default PIN
    atm = ATM(initial_balance=1000)
    # Sample interactions
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            atm.display_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == '5':
            atm.view_transaction_history()
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
