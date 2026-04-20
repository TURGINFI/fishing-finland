from django.urls import path
from .views import home_view, methods_view

urlpatterns = [
    path('', home_view, name='home'),
    path('methods/', methods_view, name='methods'),
]
