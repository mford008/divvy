from django.db import models
from divvy.users.models import User


# ('''
# This model should define share-ables, and link them to user_ids
# more functionality later...
# ''')


class ShareItem(models.Model):
    # item = models.ForeignKey(
    #     User,
    #     on_delete = models.CASCADE,
    # ),
    item_name = models.CharField(max_length=100),
    item_description = models.CharField(max_length=200),
    availability = models.CharField(max_length=100),


# class Item(models.Model):
	

