import unittest
from generator_exercise_1 import squares

class UnitTests(unittest.TestCase):

    def test_testName(self):
        self.assertEqual([n for n in squares], [x * x for x in range(1, 101)])

if __name__ == '__main__':
    unittest.TestCase
