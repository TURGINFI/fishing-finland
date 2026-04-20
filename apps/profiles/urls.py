from django.urls import path
from .views import profile_detail, profile_edit

urlpatterns = [
    path('', profile_detail, name='profile_detail'),
    path('edit/', profile_edit, name='profile_edit'),
]
