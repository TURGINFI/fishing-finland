from django.urls import path
from .views import inbox_list, mark_message_read

urlpatterns = [
    path('', inbox_list, name='inbox_list'),
    path('<int:pk>/read/', mark_message_read, name='mark_message_read'),
]
