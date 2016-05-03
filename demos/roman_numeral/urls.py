from django.conf.urls   import url
from .                  import views

app_name = 'roman_numeral'
urlpatterns = [
    url(r'result/(?P<value>\w+)$', views.result, name='result'),
    url(r'$', views.MainView.as_view(), name='index'),
]
