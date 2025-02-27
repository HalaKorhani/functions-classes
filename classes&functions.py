class Vehicle:
    def __init__(self, brand, model, year, _rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self._rental_price_per_day = _rental_price_per_day
    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self._rental_price_per_day}/day"
    def calculate_rental_cost(self, days):
        return self._rental_price_per_day * days

class Car(Vehicle):
    def __init__(self, brand, model, year, _rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, _rental_price_per_day)
        self.seating_capacity = seating_capacity
    def display_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self._rental_price_per_day}/day"
class Bike(Vehicle):
    def __init__(self, brand, model, year, _rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, _rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self._rental_price_per_day}/day"
def show_vehicle_info(vehicle):
    print(f"{vehicle.display_info()}")
vehicles = [
    Car("Toyota", "Corolla", 2020, 50, 5),
    Bike("Yamaha", "R1", 2019, 30, 998),
    Car("Honda", "Civic", 2021, 55, 5),
    Bike("Kawasaki", "Ninja", 2020, 40, 649),
]
days = int(input("Enter the number of days for rental: "))
print("Available vehicles:")
for index, vehicle in enumerate(vehicles):
    print(f"{index + 1}. {vehicle.display_info()}")
choice = int(input("Select a vehicle by number: ")) - 1
selected_vehicle = vehicles[choice]
show_vehicle_info(selected_vehicle)
print(f"Rental cost for {selected_vehicle.brand} {selected_vehicle.model} for {days} days: ${selected_vehicle.calculate_rental_cost(days)}")
