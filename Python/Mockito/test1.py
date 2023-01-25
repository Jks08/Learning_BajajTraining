from unittest import TestCase
import unittest
from mockito import when, verifyStubbedInvocationsAreUsed, unstub
import mock1

def one_plus_two():
    return mock1.add(1, 2)
class TestMockito(TestCase):
    def test_mockito(self):
        when(mock1).add(1, 2).thenReturn(3)
        self.assertEqual(3, one_plus_two())
        verifyStubbedInvocationsAreUsed()
        unstub()

if __name__ == '__main__':
    unittest.main()