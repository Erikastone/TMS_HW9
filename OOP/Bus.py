class Bus:
    def __init__(self, max_seats, max_speed):
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passenger_list = []  # Список фамилий пассажиров
        self.available_seats = max_seats  # Флаг наличия свободных мест
        self.seat_map = {}  # Словарь мест в автобусе

    def board_passenger(self, passenger_name):
        if self.available_seats > 0:
            self.passenger_list.append(passenger_name)
            self.available_seats -= 1
            print(f"{passenger_name} boarded the bus.")
        else:
            print("No available seats.")

    def disembark_passenger(self, passenger_name):
        if passenger_name in self.passenger_list:
            self.passenger_list.remove(passenger_name)
            self.available_seats += 1
            print(f"{passenger_name} disembarked from the bus.")
        else:
            print(f"{passenger_name} is not on the bus.")

    def adjust_speed(self, speed_change):
        self.max_speed += speed_change

    def __contains__(self, passenger_name):
        return passenger_name in self.passenger_list

    def __iadd__(self, passenger_name):
        self.board_passenger(passenger_name)
        return self

    def __isub__(self, passenger_name):
        self.disembark_passenger(passenger_name)
        return self

my_bus = Bus(max_seats=50, max_speed=80)
my_bus.board_passenger("Alice")
my_bus.board_passenger("Bob")
print(f"Passenger list: {my_bus.passenger_list}")
print(f"Available seats: {my_bus.available_seats}")
print(f"Is Bob on the bus? {'Bob' in my_bus}")
my_bus -= "Alice"
print(f"Passenger list after disembarking: {my_bus.passenger_list}")