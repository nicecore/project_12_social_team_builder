from django.conf.urls import url
from django.views.generic import TemplateView

from . import views



urlpatterns = [
    url(r"all/$", views.show_all_projects, name='all_projects'),
    url(r"project/new/$", views.NewProject.as_view(), name="new_project"),
    url(r"project/(?P<project_pk>\d+)/$", views.project_detail, name='project_detail'),
    url(r"project/(?P<pk>\d+)/edit/$", views.EditProject.as_view(), name='edit_project'),
    url(r"project/(?P<project_pk>\d+)/position/new/$", views.new_position, name="new_position"),
    url(r"project/(?P<project_pk>\d+)/delete/$", views.delete_project, name="delete"),
    url(r"position/(?P<position_pk>\d+)/application/new/$", views.apply, name="apply"),
    url(r"notifications/$", views.view_notifications, name="notifications"),
    url(r"applications/$", views.view_applications, name="applications"),
    url(r"applications/(?P<app_pk>\d+)/(?P<status>accept|reject)/$", views.app_status, name="app_status"),
    url(r"search/skill/(?P<skill>[a-zA-Z]+)/$", views.by_skill, name="by_skill"),
    url(r"search/$", views.search, name="search"),
    
]
