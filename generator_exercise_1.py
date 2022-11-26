import functools
import json

def json_print(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(json.dumps(result, indent=4))
        return result
    return wrapper

@json_print
def generate_json():
    example = {"SquadName": "SuperHero Squad", "HomeTown": "Metro City", 'The Greatest City': 'Disney City', 'Where Everyone is From': 'Once Upon a Time Land'}
    with open('example.json', 'w') as outfile:
        json.dump(example, outfile)
    return example

generate_json()