class Vehicle:
    def __init__(self, brand, model, year, _rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self._rental_price_per_day = _rental_price_per_day
    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self._rental_price_per_day}/day"

