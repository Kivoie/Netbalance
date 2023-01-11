from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import CustomUser
# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/


# CREATE USER
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + \
            ('email', 'first_name', 'last_name')
        is_staff = True
        is_superuser = True
        is_active = True


# LOGIN USER
class CustomUserLoginForm(AuthenticationForm):
    class Meta(AuthenticationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields  # + ('custom_field',)
        is_staff = True
        is_superuser = True
        is_active = True



