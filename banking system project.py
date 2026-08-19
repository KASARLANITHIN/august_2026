from datetime import datetime


class BankAccount:

  def __init__(self, name, account_no, balance, pin):
    self.name = name
    self.account_no = account_no
    self.__balance = balance
    self.__pin = pin
    self.mini_statement = []

  def verify_pin(self, entered_pin):
    return self.__pin == entered_pin

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      self.mini_statement.append(f"Deposit: +{amount}")
      print(f"Money deposited: {amount}")
    else:
      print("Invalid amount entered!")

  def withdraw(self, amount):
    if amount <= 0:
      print("Invalid amount entered!")
    elif amount <= self.__balance:
      self.__balance -= amount
      self.mini_statement.append(f"Withdraw: -{amount}")
      print(f"Money withdrawal: {amount}")
    else:
      print("Insufficient Balance!....In your account")

  def check_balance(self):
    print(f"Your balance: {self.__balance}")

  def show_mini_statement(self):
    print("\n------Mini Statement-----")
    print("---------------------------")
    if len(self.mini_statement) == 0:
      print("No Transactions")
    else:
      for transaction in self.mini_statement:
        print(transaction)
    print("----------------------------")
    print("Current balance: ", self.__balance)


class SavingAcc(BankAccount):

  def withdraw(self, amount):
    print("Saving Account")
    super().withdraw(amount)


class CurrentAcc(BankAccount):

  def withdraw(self, amount):
    print("Current Account")
    super().withdraw(amount)


# Default User Credentials
DEFAULT_NAME = "kasarla Nithin"
DEFAULT_ACCOUNT_NO = 2002
DEFAULT_PIN = 1234
INITIAL_BALANCE = 5000  # Updated initial balance

print("-" * 25)
print("   WELCOME TO UNION BANK   ")  # Updated bank name
print("-" * 25)

# Verification / Account Display
print(f"Account Holder: {DEFAULT_NAME}")
print(f"Account Number: {DEFAULT_ACCOUNT_NO}")
print(f"Initial Balance: {INITIAL_BALANCE}")
print("Date           : ", datetime.now().strftime("%d-%m-%Y"))
print("-" * 25)

print("1. Savings Account")
print("2. Current Account")
option = input("Enter the option: ")

account = None
if option == "1":
  account = SavingAcc(
      DEFAULT_NAME, DEFAULT_ACCOUNT_NO, INITIAL_BALANCE, pin=DEFAULT_PIN
  )
  print("Savings Account is created")
elif option == "2":
  account = CurrentAcc(
      DEFAULT_NAME, DEFAULT_ACCOUNT_NO, INITIAL_BALANCE, pin=DEFAULT_PIN
  )
  print("Current Account is created")
else:
  print("Invalid option selected. Exiting...")
  exit()

# ATM PIN Verification
print("-" * 25)
entered_pin = int(input("Enter your 4-digit ATM PIN: "))
if not account.verify_pin(entered_pin):
  print("Incorrect PIN! Access Denied.")
  exit()

# Bank Menu Loop
while True:
  print("\n" + "-" * 25)
  print("           BANK MENU         ")
  print("-" * 25)
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Mini Statement")
  print("5. Exit")
  choice = input("Enter choice (1-5): ")

  if choice == "1":
    amount = int(input("Enter deposit amount: "))
    account.deposit(amount)
  elif choice == "2":
    amount = int(input("Enter withdrawal amount: "))
    account.withdraw(amount)
  elif choice == "3":
    account.check_balance()
  elif choice == "4":
    account.show_mini_statement()
  elif choice == "5":
    print("----Thanks for choosing UNION BANK----")
    break
  else:
    print("Invalid option. Please try again.")