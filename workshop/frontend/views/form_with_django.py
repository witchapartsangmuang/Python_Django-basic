# import django library
from django.shortcuts import render
from django import forms
# import frontend.form or backend.form
from frontend.form import *
# import frontend.models or backend.models
from backend.models.shop_models import *

def form_with_django(request):
    context = {
        'title':'form_with_django'
    }
    # data in model
    prod = products.objects.all()
    comp_shop = companies_shop.objects.all()
    prod_type = product_types.objects.all()
    prod_photo = product_photos.objects.all()
    # form model 
    form_companies_shopForm = companies_shopForm()
    form_product_typesForm = product_typesForm()
    form_productsForm = productsForm()
    form_product_photosForm = product_photosForm()
    if request.method == 'POST':
        form_companies_shopForm = companies_shopForm(request.POST)
        if form_companies_shopForm.is_valid():
            form_companies_shopForm.save()

        form_product_typesForm = product_typesForm(request.POST)
        if form_product_typesForm.is_valid():
            form_product_typesForm.save()

        form_productsForm = productsForm(request.POST, request.FILES)
        if form_productsForm.is_valid():
            form_productsForm.save()

        form_product_photosForm = product_photosForm(request.POST)
        if form_product_photosForm.is_valid():
            form_product_photosForm.save()

    return render(request, 'frontend/form_with_django.html',{
        "context":context,
        #call data
        "prod":prod,
        "comp_shop":comp_shop,
        "prod_type":prod_type,
        "prod_photo":prod_photo,
        # call form
        "form_companies_shopForm":form_companies_shopForm,
        "form_product_typesForm":form_product_typesForm,
        "form_productsForm":form_productsForm,
        "form_product_photosForm":form_product_photosForm
        })
