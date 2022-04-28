# import django library
from django.urls import path
# import by youself
from django.urls import re_path

# import frontend.views
from frontend.views.index import index
from frontend.views.display_data_from_backend import display_data_from_backend
from frontend.views.search import search
from frontend.views.form_with_django import form_with_django
from frontend.views.edit import edit_data, show_edit_data
from frontend.views.delete import delete



urlpatterns = [
    # use re_path 
    re_path(r'^$', index, name='frontend-index'),
    re_path(r'display_data_from_backend' ,display_data_from_backend , name='frontend-display_data_from_backend'),
    re_path(r'^search', search, name='frontend-search'),
    re_path(r'^form_with_django', form_with_django, name='frontend-form_with_django'),
    re_path(r'^show_edit_data', show_edit_data, name='frontend-show_edit_data'),
    re_path(r'^edit_data', edit_data, name='frontend-edit_data'),
    re_path(r'^delete', delete, name='frontend-delete')
]
