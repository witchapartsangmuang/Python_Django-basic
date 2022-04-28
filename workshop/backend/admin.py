from django.contrib import admin
# call your models
from backend.models.shop_models import *

# create diplay on path('admin/', admin.site.urls)
# for upload multi photos or files
class PostImageAdmin(admin.StackedInline):
    model = product_photos
    extra = 2

# shop_models
class companies_shop_display(admin.ModelAdmin):
    list_display = ['id','comp_name','comp_address']
class product_types_display(admin.ModelAdmin):
    list_display = ['id','prod_type_name']
class products_display(admin.ModelAdmin):
    list_display = ['id','prod_photo','prod_name','prod_desc',"company_id","product_types_id"]

    inlines = [PostImageAdmin]

# Register your models here.
    # backend.models.shop_models
admin.site.register(companies_shop, companies_shop_display)
admin.site.register(product_types, product_types_display)
admin.site.register(products, products_display)
