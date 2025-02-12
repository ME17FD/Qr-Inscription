from django.urls import path
from .views import inscription_create, inscription_detail

urlpatterns = [
    path('', inscription_create, name='inscription_create'),
    path('<int:pk>/', inscription_detail, name='inscription_detail'),
]