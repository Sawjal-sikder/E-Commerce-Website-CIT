from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.user_registration, name='user_registration'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('verification/<int:verification_code>/', views.user_registration, name='user_registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
