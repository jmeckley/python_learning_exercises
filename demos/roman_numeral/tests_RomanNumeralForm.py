from django.test    import TestCase
from .models        import RomanNumeralForm

class RomanNumeralFormTests_valid(TestCase):

    def setUp(self):
        self.sut = RomanNumeralForm({ 'number': 10 })
        self.is_valid = self.sut.is_valid()
        
    def test_should_be_valid_when_number_is_between_1_and_3999(self):
        '''When RomanNumeralForm has a value between 1 and 3999 it should be valid'''
        result = self.is_valid

        self.assertTrue(result)

    def test_should_be_able_to_convert_number_to_roman_numeral(self):
        '''When RomanNumeralForm converts the number it should return the roman numeral'''
        result = self.sut.convert()

        self.assertEqual(result, 'X')

    def test_should_override__str__(self):
        '''When RomanNumeralForm returns it's string representation is should return the number'''
        result = str(self.sut)

        self.assertEqual(result, '10')

    def test_should_override__repr__(self):
        '''When RomanNumeralForm returns it's string representation is should return the name of the class and the number'''
        result = repr(self.sut)

        self.assertEqual(result, 'RomanNumeralForm(10)')

class RomanNumeralFormTests_invalid(TestCase):

    def tearDown(self):
        result = self.sut.is_valid()
        self.assertFalse(result)

    def test_should_be_invalid_when_number_is_not_supplied(self):
        '''When RomanNumeralForm has a value less than 1 it should be invalid'''
        self.sut = RomanNumeralForm({ 'number': None })
        
    def test_should_be_invalid_when_number_is_less_than_1(self):
        '''When RomanNumeralForm has a value less than 1 it should be invalid'''
        self.sut = RomanNumeralForm({ 'number': 0 })
        
    def test_should_be_invalid_when_number_is_greater_than_3999(self):
        '''When RomanNumeralForm has a value greater than 3999 it should be invalid'''
        self.sut = RomanNumeralForm({ 'number': 4000 })

class RomanNumeralFormTests_sanity_checks(TestCase):

    def setUp(self):
        self.sut = RomanNumeralForm({ 'number': 4000 })

    def test_should_override__str__(self):
        '''When RomanNumeralForm returns it's string representation is should return the number'''
        result = str(self.sut)

        self.assertEqual(result, '4000')

    def test_should_override__repr__(self):
        '''When RomanNumeralForm returns it's string representation is should return the name of the class and the number'''
        result = repr(self.sut)

        self.assertEqual(result, 'RomanNumeralForm(4000)')
