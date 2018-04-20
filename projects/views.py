from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views import generic
from notifications.signals import notify

from .forms import ProjectForm, PositionForm
from .models import Project, Position, Application


def show_all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


@login_required
def project_detail(request, project_pk):
    project = Project.objects.get(id=project_pk)
    positions = project.positions.all()
    return render(
        request,
        'projects/project_detail.html',
        {'project': project, 'positions': positions})


class NewProject(LoginRequiredMixin, generic.CreateView):
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


class EditProject(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = ['title', 'description', 'requirements', 'timeline', 'complete']

    def form_valid(self, form):
        if form.instance.owner == self.request.user:
            return super(EditProject, self).form_valid(form)
        else:
            raise PermissionDenied


@login_required
def new_position(request, project_pk):
    project = Project.objects.get(id=project_pk)
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.project = project
            position.save()
            return redirect('projects:project_detail', project_pk=project.id)
    else:
        form = PositionForm()
    return render(request, 'projects/new_position.html', {'form': form})


@login_required
def apply(request, position_pk):

    position = Position.objects.get(id=position_pk)
    project = position.project
    application = Application.objects.filter(
        applicant=request.user,
        position=position
    )
    if application.exists():
        return HttpResponseRedirect(reverse(
            'projects:project_detail', kwargs={'project_pk': project.id}
        ))

    Application.objects.create(
        applicant=request.user,
        position=position
    )

    notify.send(
        request.user,
        recipient=request.user,
        verb="You applied to {} in project '{}'".format(
            position.name, project.title)
    )

    notify.send(
        request.user,
        recipient=project.owner,
        verb="{} applied to the position '{}'' for project '{}'".format(
            request.user, position.name, project.title
        )
    )

    return HttpResponseRedirect(reverse('home'))


@login_required
def view_notifications(request):
    unread_notifs = request.user.notifications.unread()
    return render(request, 'projects/notifications.html', {'unread_notifs': unread_notifs})


@login_required
def view_applications(request):
    applications = Application.objects.filter(
        position__project__owner=request.user)
    return render(request, 'projects/applications.html', {'applications': applications})


@login_required
def app_status(request, app_pk, status):
    application = Application.objects.get(id=app_pk)
    position = Position.objects.get(application__id=application.id)
    if status == "accept":
        application.status = "A"
        application.save()
        position.filled = True
        position.save()
        notify.send(
            request.user,
            recipient=application.applicant,
            verb="{} accepted you for the position '{}'.".format(
                request.user,
                application.position.name
            )
        )
        notify.send(
            request.user,
            recipient=request.user,
            verb="You accepted {} for the position '{}'.".format(
                application.applicant,
                application.position
            )
        )
    if status == "reject":
        application.status = "R"
        application.save()
        notify.send(
            request.user,
            recipient="{} rejected you for the position '{}'".format(
                request.user,
                application.position.name
            )
        )
        notify.send(
            request.user,
            recipient="You rejected {} for the position '{}'".format(
                request.user,
                application.position.name
            )
        )
    return HttpResponseRedirect(reverse('home'))


@login_required
def delete_project(request, project_pk):
    project = Project.objects.get(id=project_pk)
    if request.user == project.owner:
        project.delete()
        return HttpResponseRedirect(reverse('home'))
    else:
        raise PermissionDenied


def search(request):
    term = request.GET.get('q')
    projects = Project.objects.filter(
        Q(title__icontains=term) | Q(description__icontains=term)
    )
    return render(request, "projects/search.html", {"projects": projects})


def by_skill(request, skill):
    projects = Project.objects.filter(positions__skill__name=skill)
    print("output: {}".format(projects))
    return render(request, "projects/search.html", {'projects': projects})
