from django.urls import path
from .views import spot_list

urlpatterns = [path('', spot_list, name='spot_list')]
