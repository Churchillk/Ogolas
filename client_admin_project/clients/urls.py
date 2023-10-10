from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_client, name='register_client'),
    path('client_list/', views.client_list, name='client_list'),
]
