from django.db import models
from django import forms
from .models import Profile
from django.contrib.auth.models import User

class Message(models.Model):
    content = models.TextField()

    def _str_(self):
        return self.content

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")