from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# from divvy.users.models import User

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
        related_name="is_member",
    )

    def __str__(self):
        return self.username

class ShareItem(models.Model):
    # item = models.ForeignKey(
    #     User,
    #     on_delete = models.CASCADE,
    # ),
    item_name = models.CharField(max_length=100),
    item_description = models.CharField(max_length=200),
    availability = models.CharField(max_length=100),

    def __str__(self):
        return self.username