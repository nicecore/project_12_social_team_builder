from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic

from .forms import ProjectForm, PositionForm
from .models import Project, Position



def show_all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def project_detail(request, project_pk):
    project = Project.objects.get(id=project_pk)
    return render(request, 'projects/project_detail.html', {'project': project})


class NewProject(generic.CreateView):
    """CBV for creating a new Project instance"""
    form_class = ProjectForm
    success_url = reverse_lazy('home')
    template_name = "projects/new_project.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(NewProject, self).form_valid(form)

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super(NewProject, self).form_valid(form)

def new_position(request, project_pk):
    project = Project.objects.get(id=project_pk)
    pass
    # Look up how to create a new instance in FBVs again... :(

class EditProject(generic.UpdateView):
    model = Project
    fields = ['title', 'description', 'requirements', 'timeline', 'complete']
