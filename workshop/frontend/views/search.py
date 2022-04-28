# import django library
from django.shortcuts import render
from django.db.models import Q
# import frontend.models or backend.models
from backend.models.shop_models import *

def search(request):
    context = {
        'title':'search'
    }
    
    prod = products.objects.all()
    prod_comp = companies_shop.objects.all()
    prod_types = product_types.objects.all()
    order_by = request.GET.get('order_by')
    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')

    if search:
        prod_comp = prod_comp.filter(comp_name__contains=search)
        # for i in prod_comp:
        #     print(i.comp_name,file=sys.stderr)
        # prod.exclude(prod_name__contains=search, company_id.)
        prod = prod.filter(Q(prod_name__contains=search) | Q(company_id__comp_name__contains=search))

    if order_by == 'high':
        if  sort_by == 'id':
            prod.order_by('-id')
        elif  sort_by == 'company_id':
            prod.order_by('-company_id')
        elif  sort_by == 'product_types_id':
            prod.order_by('-product_types_id')
        else:
            pass

    elif order_by == 'low':
        if  sort_by == 'id':
            prod.order_by('id')
        elif  sort_by == 'company_id':
            prod.order_by('company_id')
        elif  sort_by == 'product_types_id':
                prod.order_by('product_types_id')
        else:
            pass
    else:
        pass

    return render(request, 'frontend/display_data_from_backend.html',{
        "context":context,
        "prod":prod,
        "order_by":order_by,
        "sort_by":sort_by
        })