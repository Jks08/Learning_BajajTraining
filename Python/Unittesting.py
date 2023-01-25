# Unit testing in python is done using assert statements. It can also be done using unittest module.

# x = int(input("Enter a number: "))
# try:
#     assert x > 0, "Kya kar raha hai bhai? Negative number toh nahi daal sakta. Tu ek number ka dogla hai. :P"
#     print("You entered a positive number")
# except AssertionError as msg:
#     print(msg)

# import unittest # Importing unittest module 


# assertEqual(a, b) # a == b
# assertNotEqual(a, b) # a != b
# assertTrue(x) # bool(x) is True
# assertFalse(x) # bool(x) is False
# assertIs(a, b) # a is b
# assertIsNot(a, b) # a is not b
# assertIsNone(x) # x is None
# assertIsNotNone(x) # x is not None
# assertIn(a, b) # a in b
# assertNotIn(a, b) # a not in b
# assertIsInstance(a, b) # isinstance(a, b)
# assertNotIsInstance(a, b) # not isinstance(a, b)

# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()

import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = self.calc.subtract(4, 2)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calc.divide(4, 2)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, self.calc.divide, 2, 0)

if __name__ == '__main__':
    unittest.main()
