from django.db.models import ExpressionWrapper, F, FloatField, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from store.models import Cart, CartIterm
from store.serializers import (CartItemSerializer, CartSerializer,
                               CollectionSerializer, CreateCartItemSerializer,
                               ProductSerializer)

from .models import Collection, Product


# Create your views here.
def home(request):
    # return HttpResponse("Hello Ganesh Kunwar")
    from store.models import Product

    # products= Product.objects.all()
    discounted_price=ExpressionWrapper(F("unit_price") * .9,output_field=FloatField())
    total_count=Product.objects.count()
    products= Product.objects.select_related("collection").annotate(discount_price=discounted_price).order_by("-inventory") 
    

    return render(request,'home.html',{"total_products":total_count,"products": list(products)})

# controller ho yo
@api_view()
def hello(request):
    return Response("Hello Ganesh ")




class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



class CartViewSet(ModelViewSet):
    http_method_names=['get','post','delete']
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class CartItemsViewSet(ModelViewSet):
    # queryset=CartIterm.objects.all()
    # serializer_class=CartItemSerializer
    
    def get_queryset(self):
        return CartIterm.objects.filter(cart_id=self.kwargs['cart_pk'])
    
    def get_serializer_class(self):
        if self.request.method=="POST":
            return CreateCartItemSerializer
        return CartItemSerializer

        # else:
        #     return CartItemSerializer


# serializers concept here
# @api_view(['GET','POST'])
# def product_list(request):
    # products=Product.objects.select_related('collection').all()[:10]
    # serializer=ProductSerializer(products,many=True)
    # return Response(serializer.data)

# @api_view()
# def collection_list(request):
#     collections=Collection.objects.all()
#     serializer=CollectionSerializer(collections,many=True)
#     return Response(serializer.data)

# @api_view(['PUT','PATCH','DELETE'])
# def product_detail(request,id):
    
#     product=get_object_or_404(Product, id=id)
#     serializer=ProductSerializer(product)
#     return Response(serializer.data)

# class ProductList(APIView):
#     def get(self,request):
#         products=Product.objects.all()[:10]
#         serializer=ProductSerializer(products,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         data=request.data
#         serializer=ProductSerializer(data=data)
#         try:
#             serializer.is_valid()
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         except :
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view()
# def collection_detail(request,id):
#     collection=get_object_or_404(Collection,id=id)
#     serializer=CollectionSerializer(collection)
#     return Response(serializer.data)
#     # try:
#     #     product=Product.objects.get(id=id)
#     #     serializer=ProductSerializer(product)
#     #     return Response(serializer.data)
#     # except Product.DoesNotExist:
#     #     return Response({"Error":"Product Not Found"},status=status.HTTP_404_NOT_FOUND)
