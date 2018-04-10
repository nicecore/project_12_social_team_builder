from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic

from projects.models import Project


class HomeView(generic.TemplateView):
    template_name = "projects/projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context
