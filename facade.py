# Facade Pattern
# Imagine walking into a hotel. Instead of speaking to the chef, cleaner, and receptionist separately, you deal with one person at the front desk.
# The Facade pattern provides a simplified interface to a complex subsystem.

class Hotel:
    def __init__(self):
        self.chef = Chef()
        self.cleaner = Cleaner()
        self.receptionist = Receptionist()

    def check_in(self):
        self.receptionist.check_in()

    def check_out(self):
        self.receptionist.check_out()

    def order_food(self):
        self.chef.prepare_food()

    def clean_room(self):
        self.cleaner.clean_room()

    def book_room(self):
        print("Booking room")

class Chef:
    def prepare_food(self):
        print("Preparing food")

class Receptionist:
    def check_in(self):
        print("Checking in")

    def check_out(self):
        print("Checking out")

class Cleaner:
    def clean_room(self):
        print("Cleaning room")


class Airport:
    def check_in(self):
        print("Checking in")

    def board_flight(self):
        print("Boarding flight")

class Airline:
    def book_ticket(self):
        print("Booking ticket")

    def fly(self):
        print("Flying")

class Flight:
    def __init__(self):
        self.airport = Airport()
        self.airline = Airline()

    def book_ticket(self):
        self.airline.book_ticket()

    def check_in(self):
        self.airport.check_in()

    def board_flight(self):
        self.airport.board_flight()

    def fly(self):
        self.airline.fly()

class TravelFacade:
    def __init__(self):
        self.hotel = Hotel()
        self.flight = Flight()

    def plan_trip(self):
        self.hotel.book_room()
        self.hotel.check_in()
        self.hotel.order_food()
        self.hotel.clean_room()
        self.hotel.check_out()

        self.flight.book_ticket()
        self.flight.check_in()
        self.flight.board_flight()
        self.flight.fly()

# Usage
facade = TravelFacade()
facade.plan_trip()