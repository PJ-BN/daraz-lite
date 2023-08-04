from django.urls import path
from .views import *

urlpatterns = [
    path('', landing ,name = "landign"),
    path('home', home, name = "home"),
    path('profile', profile, name = "profile"),
    path('cart', cart, name = "cart")
    
]