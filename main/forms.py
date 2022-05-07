
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms

from main.models import Submission

class UserSignupForm(UserCreationForm):
    class Meta:
        fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2',)
        model = User


class SubmissionForm(forms.ModelForm):
    solution = forms.CharField(widget=forms.Textarea(attrs={'class': 'solution_input'}))
    class Meta:
        fields = ('solution',)
        model = Submission
