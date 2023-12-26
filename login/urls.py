from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('seller/login/', views.login, name='seller_login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('signup', views.signup, name='signup'),
    path('seller/signup', views.signup, name='seller_signup'),
    
    
    
]