
''' A Bird class is a parent of the Duck class. '''

class Bird:

    def call(self):
        print('chirp')

class Duck(Bird):

    def call(self):
        print('quack')

# the_bird = Bird()
# print(the_bird.call())
#
# the_duck = Duck()
# print(the_duck.call())