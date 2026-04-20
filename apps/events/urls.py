from django.urls import path
from .views import event_list, event_detail, register_for_event, my_events

urlpatterns = [
    path('', event_list, name='event_list'),
    path('my/', my_events, name='my_events'),
    path('<int:pk>/', event_detail, name='event_detail'),
    path('<int:pk>/register/', register_for_event, name='register_for_event'),
]
