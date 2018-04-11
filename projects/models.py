from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse





class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    timeline = models.CharField(max_length=200, blank=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return "{}, by {}".format(self.title, self.owner)

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'project_pk': self.id})


class Position(models.Model):
    project = models.ForeignKey(Project, related_name='positions')
    name = models.CharField(max_length=200)
    description = models.TextField()
    skill = models.ForeignKey('accounts.Skill', blank=True)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return "{} for {}, a project owned by {}".format(self.name, self.project.title, self.project.owner)


class Application(models.Model):
    STATUS_CHOICES = (
        ('A', 'Applied'),
        ('S', 'Selected'),
        ('D', 'Denied'),
    )
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    position = models.ForeignKey(Position)
    accepted = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')


    def __str__(self):
        return "{}'s application to {}".format(self.applicant, self.position)
