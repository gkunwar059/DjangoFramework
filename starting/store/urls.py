
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home),
    
    path('hello/', views.hello),
    path('product-list/', views.product_list),
    path('product-detail/<int:id>/', views.product_detail),
    path('collection-list/', views.collection_list),
    path('collection-detail/<int:id>/', views.collection_detail)
    
]
