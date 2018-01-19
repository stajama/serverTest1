from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('setter', views.setter, name="setter"),
    re_path('setter2', views.setter2, name="setter2"),
    path('setter3', views.setter3, name='setter3'),
    path('guesser', views.guesser,name='guesser'),
    re_path('guesser2', views.guesser2, name='guesser2'),
    path('guesser3', views.guesser3, name='guesser3'),
]
