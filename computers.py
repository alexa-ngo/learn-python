def make_computer(size, *equipments):
    """ Summarize the computer we are about to make. """
    print(f"\nMaking a {size} computer with the following equipments:")
    for equipment in equipments:
        print(f"-{equipment}")
