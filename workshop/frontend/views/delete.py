# import django library
from django.shortcuts import render, redirect
# import frontend.models or backend.models
from backend.models.shop_models import *

def delete(request):
    del_id = request.GET.get('delete')
    delete_data = products.objects.get(id=del_id)
    delete_data.delete()
    return redirect('/display_data_from_backend')
