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
    
