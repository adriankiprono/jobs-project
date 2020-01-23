from .models import *
from django import forms


class NewJobForm(forms.ModelForm):
    class Meta:
        model=Applicant
        exclude=['']