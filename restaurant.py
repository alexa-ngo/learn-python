class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self._restaurant_name = restaurant_name
        self._cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is", self._restaurant_name)
        print("The cuisine type is", self._cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")


alexa_restaurant = Restaurant('The Great Alexa Restaurant', 'everything under the sum')
alexa_restaurant.describe_restaurant()
alexa_restaurant.open_restaurant()

roger_restaurant = Restaurant('The Roger Restaurant', 'asian food')
riley_restaurant = Restaurant('The Riley Restaurant and Cheerios', 'Anything O shaped')
alexa_restaurant2 = Restaurant('The Second Restaurant', 'whatever sells a lot')

roger_restaurant.describe_restaurant()
riley_restaurant.describe_restaurant()
alexa_restaurant2.describe_restaurant()