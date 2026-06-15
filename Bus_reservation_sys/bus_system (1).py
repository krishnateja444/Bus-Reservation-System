from dataclasses import dataclass


@dataclass
class Passenger:
    name: str
    gender: str


class Bus:
    def __init__(self, bus_no, driver, arrival, departure, source, destination):
        self.bus_no = bus_no
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.source = source
        self.destination = destination

        # 32 seats
        self.seats = [None] * 32

    def reserve_seat(self, seat_no, name, gender):

        if seat_no < 1 or seat_no > 32:
            return False, "Invalid seat number"

        if self.seats[seat_no - 1] is not None:
            return False, "Seat already booked"

        self.seats[seat_no - 1] = Passenger(name, gender)

        return True, "Seat booked successfully"

    def get_available_seats(self):
        return [
            i + 1
            for i in range(32)
            if self.seats[i] is None
        ]

    def get_seat_layout(self):
        return self.seats


class BusReservationSystem:

    def __init__(self):
        self.buses = {}
        self.preload_buses()

    def preload_buses(self):

        buses = [
            ("1023", "Ravi", "06:30", "14:15",
             "Hyderabad", "Bangalore"),

            ("2045", "Kiran", "07:00", "12:45",
             "Chennai", "Coimbatore"),

            ("3087", "Manoj", "09:00", "13:30",
             "Kochi", "Trivandrum"),

            ("4109", "Suresh", "05:45", "08:30",
             "Bangalore", "Mysore"),

            ("5196", "Arun", "10:00", "16:30",
             "Vijayawada", "Tirupati")
        ]

        for bus in buses:
            obj = Bus(*bus)
            self.buses[obj.bus_no] = obj

    def get_all_buses(self):
        return list(self.buses.values())

    def get_bus(self, bus_no):
        return self.buses.get(bus_no)