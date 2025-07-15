from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from event.models import Event


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'priority']
