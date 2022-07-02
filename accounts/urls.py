from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
   
]
'''
 path('Hawaii/',views.hawaii,name='Hawaii'),
    path('Peru/',views.peru,name='Peru'),
    path('San Fransisco/',views.san,name='San Fransisco'),
    path('Bali/',views.bali,name='Bali'),
    path('Dubai/',views.dubai,name='Dubai'),
    path('Japan/',views.japan,name='Japan'),'''