from crispy_forms.bootstrap import FormActions
from crispy_forms.helper    import FormHelper
from crispy_forms.layout    import Submit
from django                 import forms
from django.core.validators import MaxValueValidator, MinValueValidator

CONST_MIN = 1
CONST_MAX = 3999

class RomanNumeralForm(forms.Form):

    number = forms.IntegerField(
        label="Enter a number",
        required=True,
        validators=[
            MinValueValidator(CONST_MIN),
            MaxValueValidator(CONST_MAX),
        ]
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-3'
    helper.add_input(Submit('convert', 'Convert', css_class='btn-primary'))

    def convert(self):
        number = self.cleaned_data.get('number')
        return RomanNumeralConverter().convert(number)

    def _get_number(self):
        return self.data.get('number')

    def __str__(self):
        return str(self._get_number())

    def __repr__(self):
        return "{}({})".format(type(self).__name__, self._get_number())

class RomanNumeralConverter:

    roman_numeral_map = (
        ('M',  1000),
        ('CM', 900),
        ('D',  500),
        ('CD', 400),
        ('C',  100),
        ('XC', 90),
        ('L',  50),
        ('XL', 40),
        ('X',  10),
        ('IX', 9),
        ('V',  5),
        ('IV', 4),
        ('I',  1)
    )

    def convert(self, number):
        '''convert integer to roman numeral'''

        assert isinstance(number, int), "Input must be a whole number"
        assert CONST_MIN <= number <= CONST_MAX, "Number must be between 1 and 3999"

        result = ""
        for numeral, integer in RomanNumeralConverter.roman_numeral_map:
            while number >= integer:
                result += numeral
                number -= integer
            
        return result
