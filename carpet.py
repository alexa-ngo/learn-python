class Rectangle:
    """
    Represents a geometric rectangle
    """

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * self._length + 2 * self._width


class Carpet:
    """
    Represents a carpet
    """

    def __init__(self, rect, cost_per_sq):
        self._size = rect
        self._cost_per_sq = cost_per_sq

    def get_size(self):
        return self._size

    def get_cost_per_sq_foot(self):
        return self._cost_per_sq

    def cost(self):
        return self._size.area() * self._cost_per_sq_foot()

