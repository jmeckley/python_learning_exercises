from django.core.urlresolvers   import reverse
from django.test                import TestCase
from .views                     import MainView
from .models                    import RomanNumeralForm

class MainViewTests(TestCase):

    def setUp(self):
        self.sut = MainView()
        self.form = RomanNumeralForm(data={'number': 10})
        self.form.is_valid()

    def test_form_valid_should_put_roman_numeral_into_view(self):
        '''When the form is valid it should convert the number to a roman numeral'''
        self.sut.form_valid(self.form)

        result = self.sut.roman_numeral
        
        self.assertEqual(result, 'X')

    def test_get_success_url_should_contain_an_empty_form(self):
        '''When getting the success url it should resolve the result url'''
        self.sut.roman_numeral = 'X'
        
        result = self.sut.get_success_url()

        self.assertEqual(result, '/result/X')
