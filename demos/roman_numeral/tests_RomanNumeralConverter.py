from django.test    import TestCase
from .models        import RomanNumeralConverter

class RomanNumeralConverterTests(TestCase):
    known_values = (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (18, 'XVIII'),
        (19, 'XIX'),
        (31, 'XXXI'),
        (38, 'XXXVIII'),
        (39, 'XXXIX'),
        (40, 'XL'),
        (50, 'L'),
        (98, 'XCVIII'),
        (100, 'C'),
        (148, 'CXLVIII'),
        (294, 'CCXCIV'),
        (312, 'CCCXII'),
        (388, 'CCCLXXXVIII'),
        (421, 'CDXXI'),
        (499, 'CDXCIX'),
        (500, 'D'),
        (528, 'DXXVIII'),
        (621, 'DCXXI'),
        (782, 'DCCLXXXII'),
        (867, 'DCCCLXVII'),
        (870, 'DCCCLXX'),
        (941, 'CMXLI'),
        (1000, 'M'),
        (1043, 'MXLIII'),
        (1110, 'MCX'),
        (1226, 'MCCXXVI'),
        (1301, 'MCCCI'),
        (1485, 'MCDLXXXV'),
        (1509, 'MDIX'),
        (1607, 'MDCVII'),
        (1754, 'MDCCLIV'),
        (1832, 'MDCCCXXXII'),
        (1993, 'MCMXCIII'),
        (1998, 'MCMXCVIII'),
        (2074, 'MMLXXIV'),
        (2152, 'MMCLII'),
        (2212, 'MMCCXII'),
        (2343, 'MMCCCXLIII'),
        (2499, 'MMCDXCIX'),
        (2574, 'MMDLXXIV'),
        (2646, 'MMDCXLVI'),
        (2723, 'MMDCCXXIII'),
        (2892, 'MMDCCCXCII'),
        (2975, 'MMCMLXXV'),
        (3051, 'MMMLI'),
        (3185, 'MMMCLXXXV'),
        (3250, 'MMMCCL'),
        (3313, 'MMMCCCXIII'),
        (3408, 'MMMCDVIII'),
        (3501, 'MMMDI'),
        (3610, 'MMMDCX'),
        (3743, 'MMMDCCXLIII'),
        (3844, 'MMMDCCCXLIV'),
        (3888, 'MMMDCCCLXXXVIII'),
        (3940, 'MMMCMXL'),
        (3999, 'MMMCMXCIX')
    )
    
    def setUp(self):
        self.sut = RomanNumeralConverter()

    def test_should_convert_known_value_to_roman_numeral(self):
        '''RomanNumeralConverter.convert_known_value_to_roman_numeral should return known result given the known input'''
       
        for integer, numeral in self.known_values:

            result = self.sut.convert(integer)
           
            self.assertEqual(numeral, result, "RomanNumeralConverter.convert({}) should return {} but did not. Actual result: {}".format(integer, numeral, result))

    def test_should_throw_assertion_error_if_number_is_0(self):
        '''RomanNumeralConverter.convert_known_value_to_roman_numeral should throw assertion error when number is zero'''
       
        self.assertRaises(AssertionError, self.sut.convert, 0)
            
    def test_should_throw_assertion_error_if_number_is_less_than_0(self):
        '''RomanNumeralConverter.convert_known_value_to_roman_numeral should throw assertion error when number is less than zero'''
        
        self.assertRaises(AssertionError, self.sut.convert, -1)

    def test_should_throw_assertion_error_if_number_is_greater_than_3999(self):
        '''RomanNumeralConverter.convert_known_value_to_roman_numeral should throw assertion error when number is greater than 3999'''
        
        self.assertRaises(AssertionError, self.sut.convert, 4000)

    def test_should_throw_assertion_error_if_number_is_a_string(self):
        '''RomanNumeralConverter.convert_known_value_to_roman_numeral should throw assertion error when number is a string'''
        
        self.assertRaises(AssertionError, self.sut.convert, '1')

    def test_should_throw_assertion_error_if_number_is_not_a_whole_number(self):
        '''RomanNumeralConverter.convert_known_value_to_roman_numeral should throw assertion error when number is 1.2'''
        
        self.assertRaises(AssertionError, self.sut.convert, 1.2)
