from things import Robot, Car

def start_things(thing_list):
    ''' Starts each thing in the thing list. '''
    for thing in thing_list:
        thing.start()

the_robot = Robot()
the_car = Car()

stuff = [the_robot, the_car]
start_things(stuff)