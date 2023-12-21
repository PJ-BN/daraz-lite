from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('profile', profile, name = "profile"),
    path('search', search, name = "search"),
    path('cart', cart, name = "cart"),
    path('buy', buy_now, name = "buy_now"),
    path('cart/update/', update_cart, name = "update_cart"),
    path('<slug:slug>', product, name = "product")   ,
    path('api/update_data/', update_data, name='updates_data'),
    path('api/delete_data/', delete_data, name='delete_data'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)