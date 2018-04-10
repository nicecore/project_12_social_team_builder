from django import forms
from django.conf import settings

from .models import Project, Position



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'requirements', 'timeline']

        # Need to figure out a solution for 'complete' later


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'description', 'skill']
