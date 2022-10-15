# Animal,  Mammal, Dog,

class Animal:

    def __init__(self, name, color, type):
        self._name = name
        self._color = color
        self._type = type

    def get_this_animal(self):
        return (self._name, self._color, self._type)


class Mammal(Animal):
    def __init__(self, name, color, type):
        super().__init__(name, color, type)

    def get_this_mammal(self):
        return (self._name, self._color, self._type)

class Dog(Animal):
    def __init__(self, name, color, type, fur_color):
        super().__init__(name, color, type)
        self._fur_color = fur_color

    def get_animal_info_with_fur(self):
        return (self._name, self._color, self._type, self._fur_color)


alexa_the_animal = Animal('Alexa', 'purple', 'unicorn')
print(alexa_the_animal)s
print(alexa_the_animal.get_this_animal())

alexa_the_mammal = Mammal('Alexa_mammal', 'pink', 'horse')
print(alexa_the_mammal)
print(alexa_the_mammal.get_this_animal())

alexa_the_dog = Dog('Alexa_dog', 'green', 'husky', 'brown')
print(alexa_the_dog)
print(alexa_the_dog.get_animal_info_with_fur())