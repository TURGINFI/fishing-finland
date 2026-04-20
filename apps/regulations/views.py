from django.shortcuts import get_object_or_404, render
from .models import FishingRegulation


def regulation_list(request):
    items = FishingRegulation.objects.all().order_by('title')
    return render(request, 'regulations/list.html', {'items': items})


def regulation_detail(request, pk):
    item = get_object_or_404(FishingRegulation, pk=pk)
    return render(request, 'regulations/detail.html', {'item': item})
