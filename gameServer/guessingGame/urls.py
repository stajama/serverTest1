from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('setter', views.setter, name="setter"),
    re_path('setter2', views.setter2, name="setter2"),
    path('guesser', views.guesser,name='guesser'),
]
