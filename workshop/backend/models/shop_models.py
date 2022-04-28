
from django.db import models
# Create your models here.

# shop_models
# ข้อมูลของบริษัทหรือผู้ผลิต
class companies_shop(models.Model):
    comp_name = models.CharField(max_length=50)
    comp_address =  models.CharField(max_length=200)
    def __str__(self):
        return str(self.comp_name)

# ข้อมูลของชนิดของสินค้าหรือบริการ
class product_types(models.Model):
    prod_type_name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.prod_type_name)

# ข้อมูลของของสินค้าหรือบริการ
class products(models.Model):
    prod_photo = models.FileField(upload_to='uploads/products_and_services_photos/',null=True,blank=True)
    prod_name = models.CharField(max_length=50)
    prod_desc = models.CharField(max_length=255)
    company_id = models.ForeignKey(companies_shop,related_name='product_types_companies_shop',null=True,blank=True,on_delete=models.PROTECT)
    product_types_id = models.ForeignKey(product_types,related_name='products_product_types',null=True,blank=True,on_delete=models.PROTECT)
    def __str__(self):
        return str(self.prod_name)
    
# สำหรับเก็บรูปหลายๆรูปของสินค้า
class product_photos(models.Model):
    multi_prod_photo = models.FileField(upload_to='uploads/products_and_services_photos/',null=True,blank=True)
    product_id = models.ForeignKey(products,related_name='product_photos_products',null=True,blank=True,on_delete=models.PROTECT)
    def __str__(self):
        return str(self.product_id)

# if you want to see your models in path('admin/', admin.site.urls), you need to call your models in admin.py
# but dont forget makemigrations backend and migrate before.
