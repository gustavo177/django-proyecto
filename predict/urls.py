from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),

    path('predict/', views.predict, name='predict'),
    path('datos_online/', views.visualizar_datos_online, name='visualizar_datos_online'),
    path('controles/', views.visualizar_controles, name='visualizar_controles'),

]
