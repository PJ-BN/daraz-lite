from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('profile', profile, name = "profile"),
    path('cart', cart, name = "cart"),
    path('<slug:slug>', product, name = "product")   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)