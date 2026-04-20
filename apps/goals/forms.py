from django import forms
from .models import FishingGoal


class FishingGoalForm(forms.ModelForm):
    class Meta:
        model = FishingGoal
        fields = ['year', 'target_fish', 'target_count', 'progress']
