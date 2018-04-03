from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = "accounts/signup.html"




# class ProfileView(generic.TemplateView):
#     # Needs to grab a user and pass it to the template so we can access their name and bio
#     pass


def show_profile(request):
    profile = request.user.userprofile
    return render(request, 'accounts/profile.html', {'profile': profile})


# def edit_profile(request):
#     form = forms.ProfileForm(instance=request.user.userprofile)
#     if request.method == "POST":
#         form = forms.ProfileForm(
#             data=request.POST,
#             instance=request.user.userprofile,
#             files=request.FILES
#         )
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('accounts:profile'))
#     return render(request, 'accounts/profile_edit.html', {'form': form})


class EditProfile(UpdateView):
    model = models.UserProfile
    fields = ['avatar', 'bio']
    success_url = reverse_lazy('accounts:profile')
