# import django library
from django.shortcuts import render
# import frontend.models or backend.models
from backend.models.shop_models import *

def index(request):
    context = {"title":"index"}
    return  render(request, 'frontend/index.html', {"context":context})