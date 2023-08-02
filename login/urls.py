from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='page'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    
    
]