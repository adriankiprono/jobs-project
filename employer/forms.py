from .models import *
from django import forms


class NewJobForm(forms.ModelForm):
    class Meta:
        model=Applicant
        exclude=['post']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'user_email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio','name','email')
