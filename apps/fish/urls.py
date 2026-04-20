from django.urls import path
from .views import fish_list, fish_detail

urlpatterns = [
    path('', fish_list, name='fish_list'),
    path('<int:pk>/', fish_detail, name='fish_detail'),
]
