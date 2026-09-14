import random
from datetime import datetime

# -------------------- TRAIN --------------------

class Train:
    def __init__(self, number, source, destination, seats):
        self.number = number
        self.source = source
        self.destination = destination
        self.seats = seats
        self.waiting_list = []

        # Create berth numbers according to available seats
        self.berths = []
        types = ["L", "M", "U", "SL", "SU"]

        for i in range(1, seats + 1):
            berth_type = types[(i - 1) % len(types)]
            self.berths.append(f"{berth_type}{i}")

    def show(self):
        print(f"Train Number : {self.number}")
        print(f"From         : {self.source}")
        print(f"To           : {self.destination}")
        print(f"Available    : {self.seats}")
        print()

    def book(self, count):
        if count > self.seats:
            return None

        self.seats -= count
        return [random.randint(100000, 999999) for _ in range(count)]

    def get_berth(self):
        if self.berths:
            return self.berths.pop(0)
        return "WL"


# -------------------- PASSENGER --------------------

class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.berth = None

    def show(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Phone  : {self.phone}")
        print(f"Berth  : {self.berth}")


# -------------------- TICKET --------------------

class Ticket:
    def __init__(self, train, passenger, pnr, date, booking_time, travel_class):
        self.train = train
        self.passenger = passenger
        self.pnr = pnr
        self.date = date
        self.booking_time = booking_time
        self.travel_class = travel_class

    def show(self):
        print("\n================================")
        print("         RAILWAY TICKET")
        print("================================")
        print(f"Train        : {self.train.number}")
        print(f"From         : {self.train.source}")
        print(f"To           : {self.train.destination}")
        print(f"Journey Date : {self.date}")
        print(f"Booking Time : {self.booking_time}")
        print(f"Class        : {self.travel_class}")
        print(f"PNR          : {self.pnr}")
        print(f"Berth        : {self.passenger.berth}")
        print("\nPassenger Details")
        self.passenger.show()
        print("================================")


# -------------------- ACCOUNT --------------------

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password


accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]


def login():
    while True:
        print("\n1. Create Account")
        print("2. Login")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            if any(a.username == username for a in accounts):
                print("Username already exists.")
            else:
                accounts.append(Account(username, password))
                print("Account created successfully.")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            for account in accounts:
                if account.username == username and account.password == password:
                    print(f"\nLogged in as {username}")
                    return

            print("Invalid username or password.")

        else:
            print("Invalid choice.")


# -------------------- INPUT FUNCTIONS --------------------

def choose_train(trains):
    while True:
        number = input("Enter Train Number: ")

        for train in trains:
            if train.number == number:
                return train

        print("Invalid train number.")


def get_ticket_count(train):
    while True:
        try:
            count = int(input("Enter Number of Tickets: "))

            if count <= 0:
                print("Number of tickets must be greater than 0.")
            elif count > train.seats:
                print(f"Only {train.seats} seats are available.")
                return count
            else:
                return count

        except ValueError:
            print("Please enter a valid number.")


def get_journey_date():
    while True:
        date = input("Enter Journey Date (DD-MM-YYYY): ")

        try:
            date_object = datetime.strptime(date, "%d-%m-%Y")

            if date_object.date() < datetime.now().date():
                print("Journey date cannot be in the past.")
            else:
                return date

        except ValueError:
            print("Invalid date. Use DD-MM-YYYY.")


def choose_class():
    classes = {
        "1": "SL",
        "2": "3AC",
        "3": "2AC",
        "4": "1AC"
    }

    print("\n----- SELECT CLASS -----")
    print("1. SL  - Sleeper")
    print("2. 3AC - AC 3 Tier")
    print("3. 2AC - AC 2 Tier")
    print("4. 1AC - AC First Class")

    while True:
        choice = input("Enter class choice: ")

        if choice in classes:
            return classes[choice]

        print("Invalid class choice.")


def get_passenger(number):
    while True:
        print(f"\nPassenger {number}")

        name = input("Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue

        try:
            age = int(input("Age: "))
            if age <= 0 or age > 120:
                print("Invalid age.")
                continue
        except ValueError:
            print("Age must be a number.")
            continue

        gender = input("Gender: ").strip()
        phone = input("Phone Number: ").strip()

        if len(phone) != 10 or not phone.isdigit():
            print("Phone number must contain exactly 10 digits.")
            continue

        return Passenger(name, age, gender, phone)


# -------------------- MAIN PROGRAM --------------------

trains = [
    Train("12737", "Tadepalligudem", "Secunderabad", 40),
    Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
    Train("22863", "Vijayawada", "Bangalore", 1)
]

print("\n===== RAILWAY RESERVATION SYSTEM =====")

login()

print("\n----- AVAILABLE TRAINS -----")
for train in trains:
    train.show()

train = choose_train(trains)
ticket_count = get_ticket_count(train)

# If there are not enough seats, offer waiting list.
if ticket_count > train.seats:
    print(f"Only {train.seats} confirmed seats are available.")
    choice = input("Do you want to join the waiting list? (Y/N): ").upper()

    if choice == "Y":
        passengers = []

        for i in range(ticket_count):
            passenger = get_passenger(i + 1)
            passengers.append(passenger)

            waiting_number = len(train.waiting_list) + 1
            train.waiting_list.append(passenger)

            print(f"{passenger.name} added to WL{waiting_number}")

    else:
        print("Booking cancelled.")

else:
    journey_date = get_journey_date()
    travel_class = choose_class()

    passengers = []

    for i in range(ticket_count):
        passengers.append(get_passenger(i + 1))

    pnrs = train.book(ticket_count)
    booking_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print("\n===== BOOKING SUCCESSFUL =====")

    for passenger, pnr in zip(passengers, pnrs):
        passenger.berth = train.get_berth()

        ticket = Ticket(
            train,
            passenger,
            pnr,
            journey_date,
            booking_time,
            travel_class
        )

        ticket.show()


# -------------------- WAITING LIST --------------------

print("\n----- WAITING LIST -----")

if not train.waiting_list:
    print("No passengers in waiting list.")
else:
    for number, passenger in enumerate(train.waiting_list, start=1):
        print(f"WL{number} - {passenger.name}")

print("\n------- THANK YOU -------")
print("------ SAFE JOURNEY -----")