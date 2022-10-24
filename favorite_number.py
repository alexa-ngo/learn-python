import json

""" 
This program asks the user for their favorite number. If the number is already stored, this program 
will report the favorite number to the user. 
"""

def favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        favorite_number = input("What is your favorite number? ")
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
            print(f"I know your favorite number! It's", favorite_number, ".")
    else:
        favorite_number = input("What is your favorite number? ")
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
            print(f"I know your favorite number! It's", favorite_number, ".")

favorite_number()