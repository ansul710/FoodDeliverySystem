from django import forms
from django.contrib.auth import forms
from user_profile.models import UserProfiles
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserProfiles
        fields = ('email', 'name', 'phone', 'password1', 'password2')


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)


class EditUserProfile(UserChangeForm):
    class Meta:
        model = UserProfiles
        fields = ('email', 'name', 'phone', 'password',)
