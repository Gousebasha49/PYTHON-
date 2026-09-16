from abc import ABC, abstractmethod
import uuid


class Passenger:

    def __init__(self, passenger_id, name):
        self.passenger_id = passenger_id
        self.name = name

    def show(self):
        print("\n PASSENGER ")
        print("Passenger ID :", self.passenger_id)
        print("Name         :", self.name)


class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Metro(Transport):

    def calculate_fare(self, distance):

        if distance <= 5:
            return 20
        elif distance <= 10:
            return 30
        elif distance <= 15:
            return 40
        elif distance <= 20:
            return 50
        else:
            return 60


class Ticket:

    def __init__(
        self,
        ticket_id,
        passenger,
        source,
        destination,
        distance,
        fare
    ):
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.source = source
        self.destination = destination
        self.distance = distance
        self.fare = fare
        self.status = "Confirmed"

    def show(self):

        print("\n")
        print("          METRO TICKET")
        print("")
        print("Ticket ID :", self.ticket_id)
        print("Passenger :", self.passenger)
        print("From      :", self.source)
        print("To        :", self.destination)
        print("Distance  :", self.distance, "KM")
        print("Fare      : ₹", self.fare)
        print("Status    :", self.status)
        print("")


class MetroPass:

    def __init__(
        self,
        pass_id,
        passenger,
        pass_type,
        price
    ):
        self.pass_id = pass_id
        self.passenger = passenger
        self.pass_type = pass_type
        self.price = price
        self.status = "Active"

    def show(self):

        print("\n")
        print("           METRO PASS")
        print("")
        print("Pass ID   :", self.pass_id)
        print("Passenger :", self.passenger)
        print("Pass Type :", self.pass_type)
        print("Price     : ₹", self.price)
        print("Status    :", self.status)
        print("")


class MetroSystem:

    def __init__(self):

        self.passengers = []
        self.tickets = []
        self.passes = []

        self.metro = Metro()

        self.stations = {
            "Miyapur": 0,
            "JNTU College": 2.1,
            "KPHB Colony": 3.7,
            "Kukatpally": 5,
            "Balanagar": 6.9,
            "Moosapet": 8.1,
            "Bharat Nagar": 9.4,
            "Erragadda": 10.7,
            "ESI Hospital": 11.7,
            "S R Nagar": 12.8,
            "Ameerpet": 14,
            "Punjagutta": 15.4,
            "Irrum Manzil": 16.4,
            "Khairatabad": 17.6,
            "Lakdi-ka-pul": 18.6,
            "Assembly": 19.5,
            "Nampally": 20.5,
            "Gandhi Bhavan": 21.4,
            "Osmania Medical College": 22.4,
            "MG Bus Station": 23.5,
            "Malakpet": 25,
            "New Market": 26.1,
            "Musarambagh": 27.2,
            "Dilsukhnagar": 28.4,
            "Chaitanyapuri": 29.6,
            "Victoria Memorial": 30.7,
            "LB Nagar": 32
        }

    def generate_id(self, prefix):

        return prefix + uuid.uuid4().hex[:6].upper()

    def find_passenger(self, passenger_id):

        for passenger in self.passengers:

            if passenger.passenger_id == passenger_id:
                return passenger

        return None

    def register_passenger(self):

        print("\n========== PASSENGER REGISTRATION ==========")

        name = input("Enter passenger name: ")

        passenger_id = self.generate_id("P")

        passenger = Passenger(
            passenger_id,
            name
        )

        self.passengers.append(passenger)

        print("\nPassenger registered successfully!")
        print("Passenger ID:", passenger_id)

    def display_stations(self):

        print("\n========== METRO STATIONS ==========")

        stations = list(self.stations.keys())

        for number, station in enumerate(stations, 1):
            print(number, ".", station)

        return stations

    def book_ticket(self):

        if not self.passengers:

            print("\nNo passengers registered.")
            return

        print("\n========== TICKET BOOKING ==========")

        passenger_id = input("Enter Passenger ID: ")

        passenger = self.find_passenger(passenger_id)

        if passenger is None:

            print("Passenger not found.")
            return

        stations = self.display_stations()

        try:

            source_number = int(
                input("\nSelect source station: ")
            )

            destination_number = int(
                input("Select destination station: ")
            )

        except ValueError:

            print("Enter valid station numbers.")
            return

        if not 1 <= source_number <= len(stations):

            print("Invalid source station.")
            return

        if not 1 <= destination_number <= len(stations):

            print("Invalid destination station.")
            return

        if source_number == destination_number:

            print("Source and destination cannot be same.")
            return

        source = stations[source_number - 1]
        destination = stations[destination_number - 1]

        distance = round(
            abs(
                self.stations[source]
                - self.stations[destination]
            ),
            2
        )

        fare = self.metro.calculate_fare(distance)

        ticket_id = self.generate_id("T")

        ticket = Ticket(
            ticket_id,
            passenger.name,
            source,
            destination,
            distance,
            fare
        )

        self.tickets.append(ticket)

        print("\nTicket booked successfully!")

        ticket.show()

    def generate_pass(self):

        if not self.passengers:

            print("\nNo passengers registered.")
            return

        print("\n========== METRO PASS ==========")

        passenger_id = input("Enter Passenger ID: ")

        passenger = self.find_passenger(passenger_id)

        if passenger is None:

            print("Passenger not found.")
            return

        print("\n1. Daily Pass - ₹100")
        print("2. Weekly Pass - ₹500")
        print("3. Monthly Pass - ₹1500")

        choice = input("Choose pass type: ")

        plans = {
            "1": ("Daily", 100),
            "2": ("Weekly", 500),
            "3": ("Monthly", 1500)
        }

        if choice not in plans:

            print("Invalid choice.")
            return

        pass_type, price = plans[choice]

        pass_id = self.generate_id("MP")

        metro_pass = MetroPass(
            pass_id,
            passenger.name,
            pass_type,
            price
        )

        self.passes.append(metro_pass)

        print("\nMetro pass generated successfully!")

        metro_pass.show()

    def menu(self):

        while True:

            print("\n======================================")
            print("   METRO PASS & TICKET MANAGEMENT")
            print("======================================")

            print("1. Register Passenger")
            print("2. Book Metro Ticket")
            print("3. Generate Metro Pass")
            print("4. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                self.register_passenger()

            elif choice == "2":

                self.book_ticket()

            elif choice == "3":

                self.generate_pass()

            elif choice == "4":

                print("\nThank you for using Metro System!")
                break

            else:

                print("Invalid choice.")


system = MetroSystem()
system.menu()