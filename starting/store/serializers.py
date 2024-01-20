from rest_framework import serializers

from .models import Cart, CartIterm, Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields= ["id","name","featured_product"]
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ["id","name","unit_price","inventory","description","collection"]
        
        

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ["id","name","unit_price"]
        
        
        
class CartItemSerializer(serializers.ModelSerializer):
    product=SimpleProductSerializer()
    
    # product calll garna kam lagxa tala ko product lai 
    class Meta:
        model=CartIterm
        fields=['id','quantity','product']
        
        
        
class CartSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)
    items=CartItemSerializer(many=True,read_only=True)
    total_price=serializers.SerializerMethodField()
    class Meta:
        model=Cart
        fields=['id','total_price','items']
        
    def get_total_price(self,cart):
        # yo chai list comprehension garera sum gareko
        return sum([item.product.unit_price*item.quantity for item in cart.items.all()])
    
    
class CreateCartItemSerializer(serializers.ModelSerializer):
    product_id=serializers.IntegerField()
    class Meta:
        model=CartIterm
        fields=['quantity','product_id']