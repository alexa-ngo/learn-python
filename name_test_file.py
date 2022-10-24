from name_dictionary import *

import unittest


class UnitTests(unittest.TestCase):
    def test_william_patrick_jon(self):
        # Failure message:
        # This test has no failure messages
        self.assertEqual(names[1], "William")
        self.assertEqual(names[2], "Patrick")
        self.assertEqual(names[3], "Jon")

    def test_tom_peter_colin(self):
        # Failure message:
        # This test has no failure messages
        self.assertEqual(names[4], "Tom")
        self.assertEqual(names[5], "Peter")
        self.assertEqual(names[6], "Colin")

    def test_sylvester_paul_chris(self):
        # Failure message:
        # This test has no failure messages
        self.assertEqual(names[7], "Sylvester")
        self.assertEqual(names[8], "Paul")
        self.assertEqual(names[9], "Chris")