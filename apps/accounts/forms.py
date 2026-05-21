from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower().strip()
        if not email:
            raise forms.ValidationError('Email is required.')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already in use.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        if password and cleaned_data.get('password2') and password != cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords do not match.')
        if password:
            validate_password(password)
        return cleaned_data
