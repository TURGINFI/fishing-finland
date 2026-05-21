from django import forms
from django.utils import timezone
from .models import FishingGoal


class FishingGoalForm(forms.ModelForm):
    class Meta:
        model = FishingGoal
        fields = ['year', 'target_fish', 'target_count', 'progress']

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = timezone.localdate().year
        if year < 2000 or year > current_year + 1:
            raise forms.ValidationError('Choose a realistic goal year.')
        return year

    def clean(self):
        cleaned_data = super().clean()
        target_count = cleaned_data.get('target_count')
        progress = cleaned_data.get('progress')
        if target_count is not None and target_count < 1:
            self.add_error('target_count', 'Target count must be at least 1.')
        if progress is not None and progress < 0:
            self.add_error('progress', 'Progress cannot be negative.')
        return cleaned_data
