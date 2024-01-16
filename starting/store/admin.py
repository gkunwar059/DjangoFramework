from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from store.models import Collection, Product, ProductImage


# @admin.register(ProductImage)
# inline function is okey here made like this follow the documentations
class ProductImageInlineAdmin(admin.TabularInline):
    model=ProductImage
    list_display=('id','product','image')
    extra=1
    # size of the images is here
    max_num=5
    min_num=1


# Register your models here.
class StatusFilter(admin.SimpleListFilter):
    title="status"
    parameter_name = "status"
    # strongly typed coded ho yo chai 
    def lookups(self, request ,model_admin) -> list[tuple[Any, str]]:
        # return super().lookups(request, model_admin)
        return [
            ("low","low"),
            ("high","High")
            ]
    
    
    def queryset(self,request,queryset):
       if self.value() == "low":
           return queryset.filter(inventory__lt=5)
       if self.value() == "high":
           return queryset.filter(inventory__gt=14)
    


# wwhen we overrdie and here the concept of the 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    actions=["clear_inventory_action"]
    list_display = ('name', 'unit_price','inventory','status')
    list_filter=(StatusFilter, )
    search_fields=('name','collection__name')
    inlines=(ProductImageInlineAdmin,)
    # search_fields=('name','collection__name')   this helps to call the collection foreign key where product will be called through the collection too
    # docorator concept in real world projects
    @admin.display(ordering="inventory")
    def status(self,product):
        if product.inventory<10:
            return "low"
        
        return "High"
        # else:
        #     return "High"
        
    @admin.action(description="clear inventory")
    def clear_inventory_action(self,request,queryset):
        queryset.update(inventory="0")
        self.message_user(request,"Sucessfully created ")
    

        
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id','name','featured_product')
    


















  
# admin.site.register(Collection)
# admin.site.register(Product,ProductAdmin)

