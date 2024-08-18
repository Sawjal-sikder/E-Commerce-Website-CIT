from django.urls import path
from . import views
urlpatterns = [
    path('', views.products, name='products'),
    path('single_product/<slug:slug>', views.single_product, name='single_product'),
    path('shop/grid/right/', views.shop_grid_right, name='shop_grid_right'),
    path('shop/grid/serch/category/<str:name>', views.search_category, name='search_category'),
    path('shop/pdf', views.some_view, name='some_view'),

]
