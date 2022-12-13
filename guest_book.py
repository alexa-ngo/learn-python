file_name = 'guest_book_new.txt'

input_name = input('What is your name? ')
with open(file_name, 'w') as file_object:
    file_object.write(input_name)
    file_object.write('\n')
