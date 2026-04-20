from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Event, EventRegistration


def event_list(request):
    events = Event.objects.order_by('start_time')
    return render(request, 'events/list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    already_registered = request.user.is_authenticated and EventRegistration.objects.filter(user=request.user, event=event).exists()
    return render(request, 'events/detail.html', {'event': event, 'already_registered': already_registered})


@login_required
def register_for_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    EventRegistration.objects.get_or_create(user=request.user, event=event)
    messages.success(request, 'You have registered for the event.')
    return redirect('my_events')


@login_required
def my_events(request):
    registrations = EventRegistration.objects.filter(user=request.user).select_related('event').order_by('-registered_at')
    return render(request, 'events/my_events.html', {'registrations': registrations})
