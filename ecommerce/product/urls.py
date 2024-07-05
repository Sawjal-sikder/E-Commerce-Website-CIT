from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('categories/<slug:slug>/', views.categories, name='categories'),
    path('search/', views.serarch, name='search'),
    path('single_product/<slug:slug>/', views.single_product, name='single_product'),

]


