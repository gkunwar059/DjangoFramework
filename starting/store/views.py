from django.db.models import ExpressionWrapper, F, FloatField, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.serializers import CollectionSerializer, ProductSerializer

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


# serializers concept here
@api_view()
def product_list(request):
    products=Product.objects.select_related('collection').all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view()
def collection_list(request):
    collections=Collection.objects.all()
    serializer=CollectionSerializer(collections,many=True)
    return Response(serializer.data)

@api_view()

def product_detail(request,id):
    
    product=get_object_or_404(Product, id=id)
    serializer=ProductSerializer(product)
    return Response(serializer.data)

    
@api_view()
def collection_detail(request,id):
    collection=get_object_or_404(Collection,id=id)
    serializer=CollectionSerializer(collection)
    return Response(serializer.data)
    # try:
    #     product=Product.objects.get(id=id)
    #     serializer=ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response({"Error":"Product Not Found"},status=status.HTTP_404_NOT_FOUND)
            