from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    # TODO manytomany

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class ShareGroup(models.Model):
    group_name = models.CharField(_("Name of Group"), blank=True, max_length=255)
    user = models.ManyToManyField(
        User,
        related_name="is_member"
    )

    def __str__(self):
        return self.username
