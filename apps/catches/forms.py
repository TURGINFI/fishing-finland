from django import forms
from .models import CatchLog


class CatchLogForm(forms.ModelForm):
    class Meta:
        model = CatchLog
        fields = ['fish_name', 'weight_kg', 'length_cm', 'location', 'caught_at', 'notes']
        widgets = {'caught_at': forms.DateInput(attrs={'type': 'date'})}
