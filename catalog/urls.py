from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('', landing ,name = "landing"),
    path('profile', profile, name = "profile"),
    path('cart', cart, name = "cart")
    
]