from .views import home_view
from django.urls import path



urlpatterns = [
    path('home', home_view, name='home_view')
]