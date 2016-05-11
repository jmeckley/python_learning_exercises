from django.test    import TestCase
from .forms        import FibonacciForm

class FibonacciFormTests_valid(TestCase):

    def setUp(self):
        self.sut = FibonacciForm({ 'number': 10 })
        self.is_valid = self.sut.is_valid()
        
    def test_should_be_valid_when_number_is_greater_than_0(self):
        '''When FibonacciForm has a value greater than 0 it should be valid'''
        result = self.is_valid

        self.assertTrue(result)

    def test_should_override__str__(self):
        '''When FibonacciForm returns it's string representation is should return the number'''
        result = str(self.sut)

        self.assertEqual(result, '10')

    def test_should_override__repr__(self):
        '''When FibonacciForm returns it's string representation is should return the name of the class and the number'''
        result = repr(self.sut)

        self.assertEqual(result, 'FibonacciForm(10)')

class FibonacciFormTests_invalid(TestCase):

    def tearDown(self):
        result = self.sut.is_valid()
        self.assertFalse(result)

    def test_should_be_invalid_when_number_is_not_supplied(self):
        '''When FibonacciForm does not hasve a value it should be invalid'''
        self.sut = FibonacciForm({ 'number': None })
        
    def test_should_be_invalid_when_number_is_less_than_1(self):
        '''When FibonacciForm has a value less than 0 it should be invalid'''
        self.sut = FibonacciForm({ 'number': -1 })
        
class FibonacciFormTests_sanity_checks(TestCase):

    def setUp(self):
        self.sut = FibonacciForm({ 'number': 4000 })

    def test_should_override__str__(self):
        '''When FibonacciForm returns it's string representation is should return the number'''
        result = str(self.sut)

        self.assertEqual(result, '4000')

    def test_should_override__repr__(self):
        '''When FibonacciForm returns it's string representation is should return the name of the class and the number'''
        result = repr(self.sut)

        self.assertEqual(result, 'FibonacciForm(4000)')
