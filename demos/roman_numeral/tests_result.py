from django.core.urlresolvers   import reverse
from django.test                import TestCase

class ResultTests(TestCase):

    def setUp(self):
        url = reverse('roman_numeral:result', kwargs={'value':'3'})
        self.response = self.client.get(url);

    def test_should_return_200_response_code(self):
        '''When rendering the result it should return response code 200'''
        self.assertEqual(self.response.status_code, 200)

    def test_should_contain_result(self):
        '''When roman_numeral it should display the roman numeral'''
        self.assertEqual(self.response.context['value'], '3') 
