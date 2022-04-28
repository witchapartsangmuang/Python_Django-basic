# import django library
from django.shortcuts import render, redirect
# import frontend.models or backend.models
from backend.models.shop_models import *

import sys


def show_edit_data(request):
    context = {
        'title':'edit'
    }
    # POST edit id
    post_id = request.GET.get('edit')

    # data from id = edit id
    data = products.objects.get(id=post_id)
    prod_type = product_types.objects.all()
    prod_comp_name = companies_shop.objects.all()
    
    return render(request, 'frontend/edit.html', {
        "context":context,
        "data":data,
        "prod_type":prod_type,
        "prod_comp_name":prod_comp_name
        })

def edit_data(request):

    prod_id = request.POST.get('prod_id')
    prod_name = request.POST.get('prod_name')
    prod_desc = request.POST.get('prod_desc')
    product_types_id = request.POST.get('product_types_id')
    company_id = request.POST.get('company_id')

    data = products.objects.get(id=prod_id)
    product_types_id_data = product_types.objects.get(id=product_types_id)
    com_data = companies_shop.objects.get(id=company_id)

    data.prod_name = prod_name
    data.prod_desc = prod_desc
    data.product_types_id = product_types_id_data
    data.company_id = com_data
    data.save()

    return redirect('/search')