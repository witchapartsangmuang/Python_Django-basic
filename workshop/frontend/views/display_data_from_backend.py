# import django library
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import frontend.models or backend.models
from backend.models.shop_models import *

def display_data_from_backend(request):
    context = {
        'title':'display_data_from_backend'
    }
    
    prod = products.objects.all()
    prod_comp = companies_shop.objects.all()
    prod_types = product_types.objects.all()

    order_by = request.GET.get('order_by')
    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')

    if  request.GET.get('search') != None:
        search = request.GET.get('search')
        prod_comp = prod_comp.filter(comp_name__contains=search)
        prod = prod.filter(Q(prod_name__contains=search) | Q(company_id__comp_name__contains=search))
    else:
        search = ""


    if order_by == 'high':
        if  sort_by == 'id':
            prod = prod.order_by('-id')
        elif  sort_by == 'company_id':
            prod = prod.order_by('-company_id')
        elif  sort_by == 'product_types_id':
            prod = prod.order_by('-product_types_id')
        else:
            pass

    elif order_by == 'low':
        if  sort_by == 'id':
            prod = prod.order_by('id')
        elif  sort_by == 'company_id':
            prod = prod.order_by('company_id')
        elif  sort_by == 'product_types_id':
            prod = prod.order_by('product_types_id')
        else:
            pass
    else:
        pass
    
    paginator = Paginator(prod, 4)
    page = request.GET.get('page')
    try:
        prod = paginator.page(page)
    except PageNotAnInteger:
        prod = paginator.page(1)
    except EmptyPage:
        prod = paginator.page(paginator.num_pages)

    return render(request, 'frontend/display_data_from_backend.html',{
        "context":context,
        "prod":prod,
        "search":search,
        "order_by":order_by,
        "sort_by":sort_by
        })
