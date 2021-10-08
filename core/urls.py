from django.urls import path
from .views import index, adega, adicionarVinho


urlpatterns = [
    path('', index, name='index'),
    path('adega/', adega, name='adega'),
    path('adicionarVinho/', adicionarVinho, name='adicionarVinho'),
]
