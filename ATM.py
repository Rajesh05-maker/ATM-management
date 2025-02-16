class ATMMachine:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        self.transaction_history = []

    def authenticate(self, entered_pin):
        """Check if the entered PIN matches the account PIN."""
        return self.pin == entered_pin

    def check_balance(self):
        """Display the current account balance."""
        return f"Your current balance is: ₹{self.balance}"

    def deposit_cash(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ₹{amount}")
            return f"₹{amount} deposited successfully."
        return "Invalid deposit amount."

    def withdraw_cash(self, amount):
        """Withdraw the specified amount if the balance is sufficient."""
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ₹{amount}")
        return f"₹{amount} withdrawn successfully."

    def change_pin(self, old_pin, new_pin):
        """Change the account PIN if the old PIN is correct."""
        if not self.authenticate(old_pin):
            return "Incorrect current PIN."
        if len(str(new_pin)) != 4 or not str(new_pin).isdigit():
            return "New PIN must be a 4-digit number."
        self.pin = new_pin
        self.transaction_history.append("PIN changed successfully.")
        return "PIN changed successfully."

    def show_transaction_history(self):
        """Display the history of all transactions."""
        if not self.transaction_history:
            return "No transactions yet."
        return "\n".join(self.transaction_history)

# Simulation
def atm_simulation():
    """Simulate an ATM machine."""
    user_pin = 1234  # Set the initial PIN
    atm = ATMMachine(pin=user_pin)

    print("Welcome to the ATM Machine!")
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print(atm.check_balance())

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                print(atm.deposit_cash(amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                print(atm.withdraw_cash(amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '4':
            try:
                old_pin = int(input("Enter current PIN: "))
                new_pin = int(input("Enter new 4-digit PIN: "))
                print(atm.change_pin(old_pin, new_pin))
            except ValueError:
                print("Invalid input. PIN must be numeric.")

        elif choice == '5':
            print("Transaction History:")
            print(atm.show_transaction_history())

        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_simulation()
