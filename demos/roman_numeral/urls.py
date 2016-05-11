from django.conf.urls   import url
from .                  import views

app_name = 'roman_numeral'
urlpatterns = [
    url(r'roman_numeral/result/(?P<value>\w+)$', views.result, name='result'),
    url(r'roman_numeral$', views.MainView.as_view(), name='index'),
]
