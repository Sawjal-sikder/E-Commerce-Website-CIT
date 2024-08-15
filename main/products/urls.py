from django.urls import path
from . import views
urlpatterns = [
    path('', views.products, name='products'),
    path('single_product/<slug:slug>', views.single_product, name='single_product'),
]
