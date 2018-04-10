from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"logout/$", views.LogoutView.as_view(), name="logout"),
    url(r"register/$", views.RegisterView.as_view(), name="register"),
    url(r"profile/(?P<pk>\d+)/$", views.show_any_profile, name="any_profile"),
    url(r"you/$", views.show_current_user_profile, name="current_user_profile"),
    url(r"profile/(?P<pk>\d+)/edit/$", views.EditProfile.as_view(), name='edit')
]
