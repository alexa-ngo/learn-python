prompt = "\nPlease tell me your age so I can respond with the price of a movie ticket. "
prompt += "\nHave a great day. Enter 'quit' to end the program. "

message = ''
while message != '0':
    message = int(input(prompt))

    if 1 < message <= 18:
        print('Your price is $5.')
    elif 18 <= message <= 30:
        print('Your price is $12.')
    elif 31 <= message <= 100:
        print('Your price is $50.')
    elif message >= 100:
        print('You are a fossil.')
    else:
        message == '1'
        print('Thanks for quiting the program.')

print('Thanks for quiting the program.')
