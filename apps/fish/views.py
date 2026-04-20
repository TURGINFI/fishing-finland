from django.shortcuts import get_object_or_404, render
from .models import FishSpecies


def fish_list(request):
    items = FishSpecies.objects.all().order_by('name')
    return render(request, 'fish/list.html', {'items': items})


def fish_detail(request, pk):
    item = get_object_or_404(FishSpecies, pk=pk)
    return render(request, 'fish/detail.html', {'item': item})
