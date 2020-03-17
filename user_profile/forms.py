from django import forms
from django.contrib.auth import forms
from user_profile.models import UserProfiles
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm


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


class RestPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(RestPasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].help_text = '<small id="emailHelp" class="form-text text-muted"><ul><li>Must be ' \
                                                 'of eight characters length.</li><li>Alphanumeric and atleast one ' \
                                                 'uppercase letter and symbol.</li></ul></small> '
        self.fields['new_password2'].help_text = ''
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'
