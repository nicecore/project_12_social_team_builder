from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView

from . import forms
from . import models


class LogoutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class RegisterView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = "accounts/signup.html"


def show_any_profile(request, pk):
    profile = models.UserProfile.objects.get(id=pk)
    skills = profile.skills.all()
    return render(
        request,
        'accounts/profile.html',
        {'profile': profile, 'skills': skills}
    )

def show_current_user_profile(request):
    profile = request.user.profile
    skills = profile.skills.all()
    return render(
        request,
        'accounts/profile.html',
        {'profile': profile, 'skills': skills}
    )


class EditProfile(LoginRequiredMixin, UpdateView):
    model = models.UserProfile
    fields = ['avatar', 'bio', 'skills']
    success_url = reverse_lazy('accounts:current_user_profile')

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(EditProfile, self).form_valid(form)
        else:
            raise PermissionDenied
