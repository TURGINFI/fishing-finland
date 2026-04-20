from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CatchLogForm
from .models import CatchLog


@login_required
def catch_list(request):
    items = CatchLog.objects.filter(user=request.user).order_by('-caught_at')
    return render(request, 'catches/list.html', {'items': items})


@login_required
def catch_create(request):
    if request.method == 'POST':
        form = CatchLogForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, 'Catch log added.')
            return redirect('catch_list')
    else:
        form = CatchLogForm()
    return render(request, 'catches/form.html', {'form': form})
