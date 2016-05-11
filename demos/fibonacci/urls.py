from django.conf.urls   import url
from .                  import views

app_name = 'fibonacci'
urlpatterns = [
    url(r'fibonacci/result/(?P<limit>\d+)$', views.result, name='result'),
    url(r'fibonacci$', views.MainView.as_view(), name='index'),
]
