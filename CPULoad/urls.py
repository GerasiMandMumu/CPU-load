from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from CPULoad import views

from .views import *

urlpatterns = [
    path('', views.CPULoad, name='home'),
]