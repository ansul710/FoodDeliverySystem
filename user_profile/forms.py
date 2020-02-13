from django import forms
from django.contrib.auth import forms
from user_profile.models import UserProfiles


class RegisterForm(forms.UserCreationForm):
    class Meta:
        model = UserProfiles
        fields = ('email', 'name', 'phone', 'password1', 'password2')
