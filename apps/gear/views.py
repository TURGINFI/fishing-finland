from django.shortcuts import render
from .models import GearRecommendation


def gear_list(request):
    items = GearRecommendation.objects.all().order_by('-is_featured', 'title')
    return render(request, 'gear/list.html', {'items': items})
