from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'avatar', 'fishing_gear', 'bio']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 13 or age > 120):
            raise forms.ValidationError('Enter an age between 13 and 120.')
        return age
