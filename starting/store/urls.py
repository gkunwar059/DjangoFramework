
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from . import views

router= DefaultRouter()
# routers.urls
router.register('products',views.ProductViewSet,basename='products')

router.register('carts',views.CartViewSet,basename="carts")

cart_router=NestedDefaultRouter(router,'carts',lookup='cart')
cart_router.register('items',views.CartItemsViewSet,basename='cart.items')

urlpatterns = [
    path('home/', views.home),
    # path('hello/', views.hello),
    # path('product-list/', views.product_list),
    # path('product-detail/<int:id>/', views.product_detail),
    # path('collection-list/', views.collection_list),
    # path('collection-detail/<int:id>/', views.collection_detail)
    # path('product-list/', views.ProductList.as_view()),
    
]
# custom and mixing  paths here
urlpatterns=urlpatterns+router.urls+cart_router.urls
