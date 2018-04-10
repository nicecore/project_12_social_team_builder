from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"logout/$", views.LogoutView.as_view(), name="logout"),
    url(r"register/$", views.RegisterView.as_view(), name="register"),
    # url(r"profile/$", views.ProfileView.as_view(), name="profile"),
    url(r"profile/$", views.show_profile, name='profile'),
    # url(r"profile/edit/$", views.edit_profile, name='edit_profile'),
    url(r"profile/(?P<pk>\d+)/edit/$", views.EditProfile.as_view(), name='edit')
]
