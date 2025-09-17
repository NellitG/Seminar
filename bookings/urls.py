from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.booking_form, name='new_booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('list/', views.booking_list, name='booking_list'),
]