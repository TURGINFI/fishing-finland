from django.urls import path
from .views import goal_list, goal_create

urlpatterns = [
    path('', goal_list, name='goal_list'),
    path('new/', goal_create, name='goal_create'),
]
