def get_formatted_name(first_name, last_name, middle_name=''):
    """ Return a full name, neatly formatted. """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# artist = get_formatted_name('Black', 'Pink')
# print(artist)
#
# new_student = get_formatted_name('Ryan', 'James', 'Jacobson')
# print(new_student)
