class Rectangle:
    """
    Represents a geometric rectangle.
    """

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * self._length + 2 * self._width

class Square(Rectangle):
    """
    Represents a geometric square.
    Inherits from Rectangle.
    """
    def __init__(self, side):
        self._length = side
        self._width = side

    def get_length(self):
        return self._length
