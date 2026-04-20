from django.urls import path
from .views import catch_list, catch_create

urlpatterns = [
    path('', catch_list, name='catch_list'),
    path('new/', catch_create, name='catch_create'),
]
