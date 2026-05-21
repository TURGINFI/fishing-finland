from django import forms
from django.utils import timezone
from .models import CatchLog


class CatchLogForm(forms.ModelForm):
    class Meta:
        model = CatchLog
        fields = ['fish_name', 'weight_kg', 'length_cm', 'location', 'caught_at', 'notes']
        widgets = {'caught_at': forms.DateInput(attrs={'type': 'date'})}

    def clean_caught_at(self):
        caught_at = self.cleaned_data['caught_at']
        if caught_at > timezone.localdate():
            raise forms.ValidationError('Catch date cannot be in the future.')
        return caught_at

    def clean_weight_kg(self):
        weight = self.cleaned_data.get('weight_kg')
        if weight is not None and weight <= 0:
            raise forms.ValidationError('Weight must be greater than zero.')
        return weight

    def clean_length_cm(self):
        length = self.cleaned_data.get('length_cm')
        if length is not None and length <= 0:
            raise forms.ValidationError('Length must be greater than zero.')
        return length
