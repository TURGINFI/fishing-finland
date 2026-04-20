from django.urls import path
from .views import gear_list

urlpatterns = [path('', gear_list, name='gear_list')]
