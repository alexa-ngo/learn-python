def build_person(list_of_celebrity):
    """ Return a dictionary of information about a person. """

    celebrity_list = []
    for each in list_of_celebrity:
        first_name = each[0]
        last_name = each[1]
        person = {'first': first_name, 'last': last_name}
        celebrity_list.append(person)
        print(celebrity_list)


celebrity1 = ['John', 'Legend']
celebrity2 = ['Brad', 'Pitt']
celebrity3 = ['Jennifer', 'Lopez']
list_of_celebrity = [celebrity1, celebrity2, celebrity3]

print(build_person(list_of_celebrity))
