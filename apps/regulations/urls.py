from django.urls import path
from .views import regulation_list, regulation_detail

urlpatterns = [
    path('', regulation_list, name='regulation_list'),
    path('<int:pk>/', regulation_detail, name='regulation_detail'),
]
