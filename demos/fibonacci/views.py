from django.core.urlresolvers       import reverse
from django.http                    import HttpResponseRedirect
from django.shortcuts               import render
from django.views.decorators.http   import require_http_methods
from django.views.generic           import FormView
from .fibonacci 					import fibonacci_sequence
from .forms 						import FibonacciForm

class MainView(FormView):
    template_name = 'fibonacci/main/index.html'
    form_class = FibonacciForm

    def form_valid(self, form):
        self.limit = form.cleaned_data['number']
        return super(MainView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('fibonacci:result', args = [self.limit])

@require_http_methods(["GET"])
def result(request, limit):

	sequence = str(fibonacci_sequence(int(limit)))
	return render(request, 'fibonacci/main/result.html', {'sequence': sequence})