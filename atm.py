from datetime import datetime

class Transaction:
    """Represents an individual financial transaction."""
    def __init__(self, trans_type: str, amount: float, balance_after: float):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.trans_type = trans_type
        self.amount = amount
        self.balance_after = balance_after

    def __str__(self):
        return f"[{self.timestamp}] {self.trans_type:<7} | Amount: ${self.amount:<8.2f} | Balance: ${self.balance_after:.2f}"


class Account:
    """Encapsulates account balance, credentials, and transaction history."""
    def __init__(self, account_number: str, holder_name: str, pin: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self._pin = pin  # Encapsulated private attribute
        self._balance = float(initial_balance)
        self.transactions: list[Transaction] = []

    def authenticate(self, input_pin: str) -> bool:
        return self._pin == input_pin

    def deposit(self, amount: float) -> tuple[bool, str]:
        if amount <= 0:
            return False, "Deposit amount must be greater than zero."
        
        self._balance += amount
        tx = Transaction("CREDIT", amount, self._balance)
        self.transactions.append(tx)
        return True, f"Successfully deposited ${amount:.2f}. New balance: ${self._balance:.2f}"

    def withdraw(self, amount: float) -> tuple[bool, str]:
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."
        if amount > self._balance:
            return False, f"Insufficient funds. Available balance: ${self._balance:.2f}"

        self._balance -= amount
        tx = Transaction("DEBIT", amount, self._balance)
        self.transactions.append(tx)
        return True, f"Successfully withdrew ${amount:.2f}. Remaining balance: ${self._balance:.2f}"

    def get_balance(self) -> float:
        return self._balance

    def get_mini_statement(self, limit: int = 5) -> list[Transaction]:
        # Returns the most recent transactions up to the limit
        return self.transactions[-limit:]


class ATM:
    """Handles the ATM interface, user sessions, and operational flow."""
    def __init__(self, bank_name: str, branch_name: str):
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.accounts: dict[str, Account] = {}

    def add_account(self, account: Account):
        self.accounts[account.account_number] = account

    def authenticate_user(self) -> Account | None:
        print(f"\n--- Welcome to {self.bank_name} ATM ({self.branch_name}) ---")
        acc_num = input("Enter Account Number: ").strip()

        if acc_num not in self.accounts:
            print("Error: Account number not found.")
            return None

        account = self.accounts[acc_num]
        attempts = 3

        while attempts > 0:
            pin = input("Enter 4-digit PIN: ").strip()
            if account.authenticate(pin):
                print(f"\nAuthentication successful! Welcome, {account.holder_name}.")
                return account
            
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")

        print("Account locked due to consecutive failed attempts.")
        return None

    def start_session(self):
        account = self.authenticate_user()
        if not account:
            return

        while True:
            print("\n==============================")
            print("          ATM MENU            ")
            print("==============================")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Mini Statement")
            print("5. Exit")
            
            choice = input("Select an option (1-5): ").strip()

            if choice == '1':
                print(f"\nCurrent Balance: ${account.get_balance():.2f}")

            elif choice == '2':
                try:
                    amount = float(input("Enter deposit amount: $"))
                    success, message = account.deposit(amount)
                    print(message)
                except ValueError:
                    print("Error: Invalid numerical input.")

            elif choice == '3':
                try:
                    amount = float(input("Enter withdrawal amount: $"))
                    success, message = account.withdraw(amount)
                    print(message)
                except ValueError:
                    print("Error: Invalid numerical input.")

            elif choice == '4':
                statement = account.get_mini_statement()
                print("\n--- Recent Transactions ---")
                if not statement:
                    print("No transactions found.")
                else:
                    for tx in statement:
                        print(tx)

            elif choice == '5':
                print(f"\nThank you for banking with {self.bank_name}. Good luck!")
                break
            else:
                print("Invalid option. Please choose between 1 and 5.")


# ==========================================
# Execution / Driver Code
# ==========================================
if __name__ == "__main__":
    # Initialize Bank ATM
    my_atm = ATM(bank_name="union Bank", branch_name="warangal")

    # Seed sample account (Account Number, Holder Name, PIN, Initial Balance)
    user_account = Account(
        account_number="3097",
        holder_name="nithin",
        pin="2002",
        initial_balance=1000.00
    )
    my_atm.add_account(user_account)

    # Launch ATM Terminal
    my_atm.start_session()