# Assignment 1
# Base class
class Flight:
    def __init__(self, flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline

    def display_info(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline: {self.airline}")

# Derived class
class ScheduledFlight(Flight):
    def __init__(self, flight_number, airline, departure_time, arrival_time):
        super().__init__(flight_number, airline)
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def display_info(self):
        super().display_info()
        print(f"Departure Time: {self.departure_time}")
        print(f"Arrival Time: {self.arrival_time}")

obj = ScheduledFlight("AI101", "Air India", "10:00 AM", "1:30 PM")
obj.display_info()
print("*"*50)


# Assignment 2
# Base class
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.person_id}")

# Derived class
class CrewMember(Person):
    def __init__(self, name, person_id, role):
        super().__init__(name, person_id)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")

# Further derived class
class Pilot(CrewMember):
    def __init__(self, name, person_id, role, license_number, rank):
        super().__init__(name, person_id, role)
        self.license_number = license_number
        self.rank = rank

    def display_info(self):
        super().display_info()
        print(f"License Number: {self.license_number}")
        print(f"Rank: {self.rank}")

pilot = Pilot("John Smith", "P12345", "Pilot", "LIC789", "Captain")
pilot.display_info()
print("*"*50)


# Assignment 3
# Base class
class Service:
    def service_info(self):
        print("General airport service.")

# Derived class
class SecurityService(Service):
    def service_info(self):
        print("Security Service.")

# Derived class
class BaggageService(Service):
    def service_info(self):
        print("Baggage Service.")

s1 = SecurityService()
s1.service_info()
s2 = BaggageService()
s2.service_info()
print("*"*50)


# Assignment 4
# Base class 1
class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Base class 2
class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number

# Derived class
class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def display_booking(self):
        print(f"Passenger Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Seat Number: {self.seat_number}")

booking = Booking("Poulomi", 26, "T123456", "20A")
booking.display_booking()