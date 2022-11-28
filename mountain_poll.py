# Instead of Mountain Poll this is about your college experience.

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response:
    name = input("What is your name? ")
    response = input("Did you enjoy your college experience? ")

    # Manipulate it here. If yes, +1.

    # Store the response in the dictionary.
    responses[name.title()] = response.lower()

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    # Polling is complete. Show the results.
    print('\n --- Poll Results ---')
    for name, response in responses.items():
        print(f"{name} thought {response}.")
