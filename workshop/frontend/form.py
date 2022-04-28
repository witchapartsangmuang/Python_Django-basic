# import django library
from django.db import models
from django import forms
from backend.models.shop_models import *

# shop_models form
class companies_shopForm(forms.ModelForm):
    comp_name = models.CharField(max_length=50)
    comp_address =  models.CharField(max_length=200)
    class Meta:
        model = companies_shop
        fields = ['comp_name', 'comp_address']
        widgets = {
            'comp_name': forms.TextInput(attrs={'placeholder': 'comp_name'}),
            'comp_address': forms.TextInput(attrs={'placeholder': 'comp_address'})
        }
class product_typesForm(forms.ModelForm):
    prod_type_name = models.CharField(max_length=100)
    class Meta:
        model = product_types
        fields = ['prod_type_name']
        widgets = {
            'prod_type_name': forms.TextInput(attrs={'placeholder': 'type'})
        }
class productsForm(forms.ModelForm):
    prod_photo = models.FileField(upload_to='uploads/products_and_services_photos/',null=True,blank=True)
    prod_name = models.CharField(max_length=50)
    prod_desc = models.CharField(max_length=255)
    company_id = models.ForeignKey(companies_shop,related_name='product_types_companies_shop',null=True,blank=True,on_delete=models.PROTECT)
    product_types_id = models.ForeignKey(product_types,related_name='products_product_types',null=True,blank=True,on_delete=models.PROTECT)
    class Meta:
        model = products
        fields = ['prod_photo', 'prod_name', 'prod_desc','company_id','product_types_id']
        widgets = {
            'prod_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'prod_desc': forms.TextInput(attrs={'placeholder': 'desc'})
        }
class product_photosForm(forms.ModelForm):
    multi_prod_photo = models.FileField(upload_to='uploads/products_and_services_photos/',null=True,blank=True)
    product_id = models.ForeignKey(products,related_name='product_photos_products',null=True,blank=True,on_delete=models.PROTECT)
    class Meta:
        model = product_photos
        fields = ['multi_prod_photo', 'product_id']