def make_car(manufacturer, model, **car_info):
    """ Build a dictionary containing everything we have about a car. """
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


def process_car(car_info, name):
    return car_info['manufacturer'] + ' belongs to ' + name


create_a_car = make_car('toyota', 'corolla', interior='leather seats', paint='high quality')
print(create_a_car)
name = 'Alexa'
results = process_car(create_a_car, name)
print(results)
