from inheritance2shapes import Square

class Cube:
    """ Represents a geometric cube. """

    def __init__(self, side):
        self._face = Square(side)

    def surface_area(self):
        return self._face.area() * 6

    def volume(self):
        return self._face.area() * self._face.get_length()



# get the length from rectangle
the_cube = Cube(3)
print(the_cube)


print("# get the surface_area from the cube")
print("Expected: 54")
print(the_cube.surface_area())


print("# get the volume from the cube")
print("Expected: 27")
print(the_cube.volume())