from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import FishingGoalForm
from .models import FishingGoal


@login_required
def goal_list(request):
    goals = FishingGoal.objects.filter(user=request.user).order_by('-year', 'target_fish')
    return render(request, 'goals/list.html', {'goals': goals})


@login_required
def goal_create(request):
    if request.method == 'POST':
        form = FishingGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Goal saved.')
            return redirect('goal_list')
    else:
        form = FishingGoalForm()
    return render(request, 'goals/form.html', {'form': form})
