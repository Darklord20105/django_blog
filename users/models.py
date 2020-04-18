from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns around the globe.
    name = models.CharField(blank=True, max_length=255)

    picture = models.ImageField(
        upload_to="profile_pics/", null=True, blank=True)

    location = models.CharField(max_length=50, null=True, blank=True)

    job_title = models.CharField(max_length=50, null=True, blank=True)

    personal_url = models.URLField(max_length=555, blank=True, null=True)

    facebook_account = models.URLField(max_length=255, blank=True, null=True)

    twitter_account = models.URLField(max_length=255, blank=True, null=True)

    github_account = models.URLField(
        max_length=255, blank=True, null=True)

    linkedin_account = models.URLField(
        max_length=255, blank=True, null=True)

    short_bio = models.CharField(max_length=60, blank=True, null=True)

    bio = models.CharField(max_length=280, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_profile_name(self):
        if self.name:
            return self.name

        return self.username
