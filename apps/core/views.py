from django.shortcuts import render
from apps.blogs.models import BlogPost
from apps.events.models import Event
from apps.gear.models import GearRecommendation


def home_view(request):
    context = {
        'latest_blogs': BlogPost.objects.filter(status=BlogPost.Status.APPROVED)[:3],
        'upcoming_events': Event.objects.order_by('start_time')[:3],
        'featured_gear': GearRecommendation.objects.filter(is_featured=True)[:3],
    }
    return render(request, 'home.html', context)


def methods_view(request):
    return render(request, 'methods.html')
