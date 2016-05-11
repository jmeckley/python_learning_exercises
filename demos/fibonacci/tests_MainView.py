from django.core.urlresolvers   import reverse
from django.test                import TestCase
from .views                     import MainView
from .forms                    import FibonacciForm

class MainViewTests(TestCase):

    def setUp(self):
        self.sut = MainView()
        self.form = FibonacciForm(data={'number': 10})
        self.form.is_valid()

    def test_form_valid_should_put_the_limit_into_view(self):
        '''When the form is valid it should put the limit in the root'''
        self.sut.form_valid(self.form)

        result = self.sut.limit
        
        self.assertEqual(result, 10)

    def test_get_success_url_should_return_the_result_url(self):
        '''When getting the success url it should resolve the result url'''
        expected = reverse('fibonacci:result', args=[10])
        self.sut.limit = 10
        
        result = self.sut.get_success_url()

        self.assertEqual(result, expected)
