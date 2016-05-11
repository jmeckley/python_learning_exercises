from crispy_forms.bootstrap import FormActions
from crispy_forms.helper    import FormHelper
from crispy_forms.layout    import Submit
from django                 import forms
from django.core.validators import MinValueValidator

class FibonacciForm(forms.Form):

    number = forms.IntegerField(
        label="Enter a number",
        required=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-3'
    helper.add_input(Submit('calculate', 'Calculate', css_class='btn-primary'))

    def _get_number(self):
        return self.data.get('number')

    def __str__(self):
        return str(self._get_number())

    def __repr__(self):
        return "{}({})".format(type(self).__name__, self._get_number())
