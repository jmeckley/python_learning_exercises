from django.core.urlresolvers   import reverse
from django.test                import TestCase

class UrlsTests(TestCase):

    def tearDown(self):
        result = self.client.get(self.url).status_code
        self.assertEqual(result, 200)

    def test_when_navigating_to_index_should_return_200_response_code(self):
        '''When accessing the roman numeral page it should return response code 200'''
        self.url = reverse('roman_numeral:index')

    def test_when_navigating_to_result_should_return_200_response_code(self):
        '''When accessing the result page it should return response code 200'''
        self.url = reverse('roman_numeral:result', args=['XI'])

