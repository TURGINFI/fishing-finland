from django.urls import path
from .views import public_blog_list, public_blog_detail, my_blog_list, blog_create

urlpatterns = [
    path('', public_blog_list, name='public_blog_list'),
    path('my/', my_blog_list, name='my_blog_list'),
    path('new/', blog_create, name='blog_create'),
    path('<int:pk>/', public_blog_detail, name='public_blog_detail'),
]
