from django.urls import path
from .views import register_view, delete_account_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('delete/', delete_account_view, name='delete_account'),
]
