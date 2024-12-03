
from django.urls import path
from task4.views import platform, games, cart

urlpatterns = [
    path('platform/', platform, name='platform'),
    path('platform/games/', games, name='games'),
    path('platform/cart/', cart, name='cart'),
]