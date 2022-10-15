class Dog:
    """ Class modeling a dog. """

    def __init__(self, name, age):
        """ Initialize name and age attribute. """
        self._name = name
        self._age = age

    def sit(self):
        """ Simulate a dog sitting in response to a command. """
        return (f"{self._name} is not sitting.")

    def roll_over(self):
        """ Simulate rolling over in response to a command. """
        return (f"{self._name} rolled over!")

the_poodle = Dog('Albert', 4)
result1 = the_poodle.sit()
result2 = the_poodle.roll_over()

print(result1)
print(result2)