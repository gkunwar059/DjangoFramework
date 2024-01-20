from uuid import uuid4

from django.db import models


# Create your models here.
    # footwear is colllection here
class Collection(models.Model):
    name=models.CharField(max_length=250)
    # foreign key must be difined withthe above  above product
    featured_product=models.ForeignKey("Product",on_delete=models.SET_NULL, null=True, related_name="+", blank=True)
    # product is not defined yet
    
    def __str__(self):
       return self.name.capitalize()    
        
    
class Product(models.Model):
    # id=models.BigAutoField(auto_increment=True)
    name=models.CharField(max_length=250)
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.PositiveBigIntegerField()
    description=models.TextField()
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    
    # collection is not deleted before deleteing the data of the product
    
    def __str__(self):
        return self.name.capitalize()
    
    
class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/store/products", null=True,blank=True)
    
# important field
# auto now  => 
class Cart(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid4)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

class CartIterm(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    quantity=models.PositiveIntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    

# class Rating(models.Model):
#     # id=models.BigIntegerField()
#     rating=models.ForeignKey(Product,on_delete=models.CASCADE ,related_name='items')
#     comment=


