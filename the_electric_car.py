class Car:
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """ Represents aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """ Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery.")


class SpaceShip(Car):
    """ Represents aspects of a car, specific to spaceships. """

    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class. """
        super().__init__(make, model, year)
        self.fuel_type = 'hydrogen'

    def describe_fuel(self):
        """ Print a statement describing the fuel type. """
        print(f"This car uses {self.fuel_type}.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())

my_rocketship = SpaceShip('metal boat', 'the accelerator', 2022)
print(my_rocketship.get_descriptive_name())
print(my_rocketship.describe_fuel())
