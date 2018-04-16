from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver




class Skill(models.Model):

    SKILL_CHOICES = (
        ('android', "Android Developer"),
        ('designer', "Designer"),
        ('java', "Java Developer"),
        ('php', "PHP Developer"),
        ('python', "Python Developer"),
        ('rails', "Rails Developer"),
        ('wordpress', "Wordpress Devloper"),
        ('ios', "iOS Developer")
    )

    name = models.CharField(choices=SKILL_CHOICES, max_length=50, default='')

    def __str__(self):
        return self.name.title()



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.user.username.title() + "'s User Profile"

# Create new UserProfile object upon creation of new User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)



