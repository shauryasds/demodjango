from django.urls import path
from .views import hello_world ,test

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('test/', test, name='test'),
]