class Car:
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self._odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self._year} {self._make} {self._model}"
        return long_name.title()

    def read_odometer(self):
        return (f"This car has {self._odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            return ("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self._odometer_reading += miles

    def fill_gas_tank(self):
        """ We will override this method in the ElectricCar class. """
        return ("This car needs gas!")

class Battery:
    """ A battery for an electric car. """

    def __init__(self, battery_size=75):
        """ Initialize the battery's attributes. """
        self._battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size. """
        print(f"This car has a {self._battery_size}-kWh battery.")

    def get_range(self):
        """ Print a statement about the range this battery provides. """
        if self._battery_size == 75:
            range = 260
        elif self._battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class EcoMode:
    """ Going ecoFriendly mode. """

    def __init__(self, eco_mode=98):
        """ Initialize the eco mode. """
        self._eco_mode = eco_mode

    def describe_eco_mode(self):
        """ Print that you're going eco-mode. """
        print(f"This car is going {self._eco_mode} percent eco-mode.")


class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year, driver_name):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self._battery = Battery()
        self._ecoMode = EcoMode()
        self._driver_name = driver_name

#     def fill_gas_tank(self):
#         """ We will override this function that is in the Parent Class. """
#         return ("This car does not need gas!")

    def describe_eco_mode(self):
        """ Override the EcoMode with this method. """
        print(f"There is no need. This car is already as green as it gets.")

    def set_driver_name(self, driver_name):
        self._driver_name = driver_name

    def get_driver_name(self):
        return self._driver_name

alexa_car = ElectricCar('tesla', 'model s', 2022, "Bob")
# alexa_car.get_descriptive_name()
# alexa_car._battery.describe_battery()
# alexa_car.describe_eco_mode()
# print(alexa_car.get_driver_name())
# print("set to Rachel")
# alexa_car.set_driver_name('Rachel')
# print(alexa_car.get_driver_name())
# alexa_car._battery.get_range()

alexa_car.update_odometer(5)
print(alexa_car.read_odometer())