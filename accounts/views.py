from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
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




# class ProfileView(generic.TemplateView):
#     # Needs to grab a user and pass it to the template so we can access their name and bio
#     pass


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


class EditProfile(UpdateView):
    model = models.UserProfile
    fields = ['avatar', 'bio', 'skills']
    success_url = reverse_lazy('accounts:current_user_profile')
