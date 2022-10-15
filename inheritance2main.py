from inheritance2shapes import Square, Rectangle

class Cube(Square):
    """
    Represents a geometric cube
    """

    def surface_area(self):
        return super().area() * 6

    def volume(self):
        return super().area() * self._length

the_cube = Cube(3)
print(the_cube)
print(the_cube.surface_area())
print(the_cube.volume())