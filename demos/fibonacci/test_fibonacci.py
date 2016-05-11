from django.test import TestCase
from .fibonacci import fibonacci, fibonacci_sequence

class FibonacciTests(TestCase):

    known_values = (
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
    )

    def test_fibonacci_for_known_values(self):
        '''fibonacci should return known result given the known input'''
       
        for limit, expected in self.known_values:
            result = fibonacci(limit)
            self.assertEqual(expected, result, "fibonacci({}) should return {} but did not. Actual result: {}".format(expected, limit, result))

    def test_fibonacci_sequence_with_7(self):
        '''when limit is 7 fibonacci_sequence should return [0,1,1,2,3,5,8,13]'''
       
        expected = [0,1,1,2,3,5,8,13]

        result = fibonacci_sequence(7)

        self.assertEqual(expected, result)