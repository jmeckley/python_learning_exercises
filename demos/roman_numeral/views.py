from django.core.urlresolvers       import reverse
from django.http                    import HttpResponseRedirect
from django.shortcuts               import render
from django.views.decorators.http   import require_http_methods
from django.views.generic           import FormView
from .models                        import RomanNumeralForm

class MainView(FormView):
    template_name = 'main/index.html'
    form_class = RomanNumeralForm

    def form_valid(self, form):
        self.roman_numeral = form.convert()
        return super(MainView, self).form_valid(form)

    def get_success_url(self, **kwargs):         
        return reverse('roman_numeral:result', args = [self.roman_numeral])

    
@require_http_methods(["GET"])
def result(request, value):
    return render(request, 'main/result.html', { 'value': value })
