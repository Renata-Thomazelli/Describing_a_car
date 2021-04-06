""" A class to represent a car"""

class Car:
    """A simple attempt to represent a car."""
    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0
        self.gas_tank = 45
        
    def get_descriptive_name(self):
        """Retorn a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value.  
        Reject the change if it attempts to roll the odometer back."""
        if mileage >=self. odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
        
    def fill_gas_tank(self):
        """Describe how much is necessary to fill the fas tank."""
        print(f" The capacit of the gas tank is {self.gas_tank} l.")

        
