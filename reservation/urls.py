from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
]