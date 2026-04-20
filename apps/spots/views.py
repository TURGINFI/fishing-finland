from django.shortcuts import render
from .models import FishingSpot


def spot_list(request):
    items = FishingSpot.objects.all().order_by('area', 'name')
    return render(request, 'spots/list.html', {'items': items})
