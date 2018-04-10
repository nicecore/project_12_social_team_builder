from django import forms

from .models import Project, Position



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['avatar', 'bio']
